"""
Shopify Store Deals Scraper (Deux par Deux, Stonz, Konny)
Fetches real-time Canadian prices, discounts, and inventory status.
"""

import urllib.request
import json
import logging
from typing import List, Dict
from config import SHOPIFY_STORES
from filters.deal_evaluator import is_baby_girl_relevant, detect_category, score_deal

logger = logging.getLogger(__name__)

class ShopifyScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8"
        }

    def fetch_collection_products(self, base_url: str, collection_handle: str, limit: int = 50) -> List[Dict]:
        """Fetches products.json from a Shopify collection."""
        url = f"{base_url}/collections/{collection_handle}/products.json?limit={limit}"
        req = urllib.request.Request(url, headers=self.headers)
        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8", errors="ignore"))
                    return data.get("products", [])
        except Exception as e:
            logger.warning(f"Failed to fetch Shopify collection {collection_handle} from {base_url}: {e}")
        return []

    def scrape_store(self, store_key: str, min_discount: float = 15.0) -> List[Dict]:
        """Scrapes all configured collections for a specific Shopify brand."""
        store_config = SHOPIFY_STORES.get(store_key)
        if not store_config:
            return []

        base_url = store_config["base_url"]
        brand_name = store_config["name"]
        results = []
        seen_handles = set()

        for col in store_config["collections"]:
            handle = col["handle"]
            default_cat = col["category"]
            products = self.fetch_collection_products(base_url, handle, limit=50)

            for prod in products:
                prod_handle = prod.get("handle")
                if prod_handle in seen_handles:
                    continue

                title = prod.get("title", "")
                tags = prod.get("tags", [])
                body_html = prod.get("body_html", "") or ""

                # Baby girl relevance filter
                if not is_baby_girl_relevant(title, body_html, tags):
                    continue

                # Process variants to find pricing and sizes
                variants = prod.get("variants", [])
                if not variants:
                    continue

                # Collect sizes and available stock
                available_sizes = []
                best_variant = None
                highest_discount = -1.0

                for v in variants:
                    price = float(v.get("price") or 0.0)
                    compare_at = float(v.get("compare_at_price") or price)
                    is_avail = v.get("available", True)
                    size_title = v.get("title", "")

                    if is_avail and size_title not in ["Default Title", ""]:
                        available_sizes.append(size_title)

                    disc = (1.0 - price / compare_at) * 100 if compare_at > price else 0.0
                    if disc > highest_discount or best_variant is None:
                        highest_discount = disc
                        best_variant = (price, compare_at, is_avail)

                if not best_variant:
                    continue

                price, original_price, is_available = best_variant

                # Skip if no discount or below threshold
                deal_info = score_deal(price, original_price, brand_name)
                if deal_info["discount_pct"] < min_discount:
                    continue

                # Image
                images = prod.get("images", [])
                image_url = images[0].get("src", "") if images else ""

                category = detect_category(title, default_cat)
                product_url = f"{base_url}/products/{prod_handle}"

                item = {
                    "id": f"{store_key}_{prod.get('id')}",
                    "brand": brand_name,
                    "brand_key": store_key,
                    "title": title,
                    "price_cad": round(price, 2),
                    "original_price_cad": round(original_price, 2),
                    "discount_pct": deal_info["discount_pct"],
                    "savings_cad": deal_info["savings_cad"],
                    "badge": deal_info["badge"],
                    "stars": deal_info["stars"],
                    "value_tier": deal_info["value_tier"],
                    "category": category,
                    "sizes": available_sizes[:5],
                    "in_stock": is_available,
                    "product_url": product_url,
                    "image_url": image_url,
                    "source": "Shopify Live API",
                    "collection": col["name"]
                }

                results.append(item)
                seen_handles.add(prod_handle)

        return results

    def scrape_all(self, min_discount: float = 15.0) -> List[Dict]:
        """Scrapes all supported Shopify stores."""
        all_deals = []
        for store_key in SHOPIFY_STORES.keys():
            deals = self.scrape_store(store_key, min_discount=min_discount)
            all_deals.extend(deals)
        return all_deals
