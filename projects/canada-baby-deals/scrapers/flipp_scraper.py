"""
Flipp Canada Flyer & Retail Clearance Scraper (Carter's, Walmart CA, Toys R Us, etc.)
Retrieves live flyer promotions, Black Friday doorbusters, and store clearances across Canada.
"""

import urllib.request
import urllib.parse
import json
import logging
from typing import List, Dict
from config import DEFAULT_POSTAL_CODE, FLIPP_SEARCHES
from filters.deal_evaluator import is_baby_girl_relevant, detect_category, score_deal

logger = logging.getLogger(__name__)

class FlippCanadaScraper:
    BASE_URL = "https://backflipp.wishabi.com/flipp/items/search"

    def __init__(self, postal_code: str = DEFAULT_POSTAL_CODE):
        self.postal_code = postal_code.replace(" ", "")
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json"
        }

    def search_query(self, query: str, category: str, default_brand: str, min_discount: float = 15.0) -> List[Dict]:
        """Searches Flipp Canada catalog for specific keywords."""
        params = {
            "postal_code": self.postal_code,
            "q": query
        }
        url = f"{self.BASE_URL}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers=self.headers)
        results = []

        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8", errors="ignore"))
                    ecom_items = data.get("ecom_items", [])
                    flyer_items = data.get("items", [])

                    # Parse e-commerce clearance items
                    for item in ecom_items:
                        parsed = self._parse_ecom_item(item, category, default_brand, min_discount)
                        if parsed:
                            results.append(parsed)

                    # Parse flyer promotional items
                    for item in flyer_items:
                        parsed = self._parse_flyer_item(item, category, default_brand, min_discount)
                        if parsed:
                            results.append(parsed)

        except Exception as e:
            logger.warning(f"Error querying Flipp with query '{query}': {e}")

        return results

    def _parse_ecom_item(self, item: dict, default_cat: str, default_brand: str, min_discount: float) -> dict:
        title = item.get("name") or ""
        desc = item.get("description") or ""

        if not is_baby_girl_relevant(title, desc):
            return None

        current_price = float(item.get("current_price") or 0.0)
        original_price = float(item.get("original_price") or current_price)

        if current_price <= 0:
            return None

        deal_info = score_deal(current_price, original_price, default_brand)
        if deal_info["discount_pct"] < min_discount:
            return None

        merchant = item.get("merchant") or "Canadian Retailer"
        brand_name = default_brand if default_brand != "Multi-Brand" else merchant

        # Determine best category
        category = detect_category(title, default_cat)

        # Build product link (Flipp or merchant search)
        sku = item.get("item_id") or ""
        product_url = f"https://www.walmart.ca/en/ip/{sku}" if merchant == "Walmart" and sku else f"https://flipp.com/en-ca/search/{urllib.parse.quote(title[:40])}"

        return {
            "id": f"flipp_ecom_{item.get('id', item.get('global_id_int'))}",
            "brand": f"{brand_name} ({merchant})",
            "brand_key": "flipp",
            "title": title,
            "price_cad": round(current_price, 2),
            "original_price_cad": round(original_price, 2),
            "discount_pct": deal_info["discount_pct"],
            "savings_cad": deal_info["savings_cad"],
            "badge": deal_info["badge"],
            "stars": deal_info["stars"],
            "value_tier": deal_info["value_tier"],
            "category": category,
            "sizes": [],
            "in_stock": True,
            "product_url": product_url,
            "image_url": item.get("image_url") or "",
            "source": f"Flyer & Clearance: {merchant}",
            "collection": f"Flipp Deal Search: {default_cat}"
        }

    def _parse_flyer_item(self, item: dict, default_cat: str, default_brand: str, min_discount: float) -> dict:
        title = item.get("name") or ""
        desc = item.get("description") or ""

        if not is_baby_girl_relevant(title, desc):
            return None

        current_price = float(item.get("current_price") or 0.0)
        original_price = float(item.get("original_price") or current_price)

        if current_price <= 0:
            return None

        deal_info = score_deal(current_price, original_price, default_brand)
        if deal_info["discount_pct"] < min_discount:
            return None

        merchant = item.get("merchant_name") or "Canadian Flyer"
        category = detect_category(title, default_cat)

        return {
            "id": f"flipp_flyer_{item.get('id')}",
            "brand": f"{default_brand} ({merchant})",
            "brand_key": "flipp",
            "title": title,
            "price_cad": round(current_price, 2),
            "original_price_cad": round(original_price, 2),
            "discount_pct": deal_info["discount_pct"],
            "savings_cad": deal_info["savings_cad"],
            "badge": deal_info["badge"],
            "stars": deal_info["stars"],
            "value_tier": deal_info["value_tier"],
            "category": category,
            "sizes": [],
            "in_stock": True,
            "product_url": f"https://flipp.com/en-ca/search/{urllib.parse.quote(title[:40])}",
            "image_url": item.get("clean_image_url") or "",
            "source": f"Weekly Flyer: {merchant}",
            "collection": f"Flyer Special: {default_cat}"
        }

    def scrape_all(self, min_discount: float = 15.0) -> List[Dict]:
        """Runs all configured searches across Canadian flyers and clearance databases."""
        all_deals = []
        seen_titles = set()

        for config in FLIPP_SEARCHES:
            deals = self.search_query(
                query=config["query"],
                category=config["category"],
                default_brand=config["brand"],
                min_discount=min_discount
            )
            for d in deals:
                short_title = d["title"][:50].lower()
                if short_title not in seen_titles:
                    all_deals.append(d)
                    seen_titles.add(short_title)

        return all_deals
