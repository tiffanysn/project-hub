"""
Curated Brand Deals & Black Friday / December Promotional Strategies for Canada
Covers: Gap Canada, Zara Canada, H&M Canada, and Carter's OshKosh Canada.
"""

from typing import List, Dict

CURATED_BRAND_GUIDES = [
    {
        "brand": "Gap Canada",
        "official_url": "https://www.gapcanada.ca/browse/category.do?cid=65217",
        "sale_section_name": "Baby Girl Sale & Clearance (0-24M)",
        "bf_strategy": "黑五全场 50% OFF + 额外 10% OFF 折上折，12月双旦年终清仓低至 3 折",
        "best_picks": "连体衣 (Bodysuits)、针织开衫 (Cardigans)、加绒卫裤 (Fleece Pants)"
    },
    {
        "brand": "Zara Canada",
        "official_url": "https://www.zara.com/ca/en/kids-babygirl-special-prices-l414.html",
        "sale_section_name": "Baby Girl Special Prices & Boxing Day Sale",
        "bf_strategy": "黑五精选 40% OFF（黑五前夕 8:00 PM App 抢先开抢）；12月25日 Boxing Day 开启全季大清仓（3-5折）",
        "best_picks": "设计款连衣裙、针织毛衣、复古软底学步鞋、羊羔绒外套"
    },
    {
        "brand": "H&M Canada",
        "official_url": "https://www2.hm.com/en_ca/baby/sale/baby-girl.html",
        "sale_section_name": "H&M Baby Girl Sale",
        "bf_strategy": "会员黑五全场 25%~30% OFF 免运费；12月节前每日特惠 (Holiday Countdown) 及年末折上折",
        "best_picks": "纯棉多件装连体衣（包屁衣组合性价比极高）、荷叶边连体裙、家居爬服"
    },
    {
        "brand": "Carter's OshKosh Canada",
        "official_url": "https://www.cartersoshkosh.ca/en_CA/carters-baby-girl-clearance",
        "sale_section_name": "Carter's Canada Official Baby Girl Clearance",
        "bf_strategy": "黑五全场 50%~60% OFF + 门票爆款 (Doorbusters $5~$9 CAD) + 全场包邮",
        "best_picks": "纯棉睡袋 (Sleep & Play)、节日红/格纹连体裙、节日家居套装"
    }
]

CURATED_HOT_DEALS = [
    {
        "id": "curated_gap_01",
        "brand": "Gap Canada",
        "brand_key": "gap",
        "title": "Baby 100% Organic Cotton Floral Bodysuit & Pant Set",
        "price_cad": 19.99,
        "original_price_cad": 44.95,
        "discount_pct": 55.5,
        "savings_cad": 24.96,
        "badge": "🔥 超级神价 (Steal)",
        "stars": "⭐⭐⭐⭐⭐",
        "value_tier": "ultra_high",
        "category": "clothes",
        "sizes": ["0-3M", "3-6M", "6-12M", "12-18M"],
        "in_stock": True,
        "product_url": "https://www.gapcanada.ca/browse/category.do?cid=65217",
        "image_url": "https://www.gapcanada.ca/Asset_Archive/GPWeb/assets/common/gap-logo.png",
        "source": "Gap Canada Official BF Deal",
        "collection": "Gap Baby Girl Deals"
    },
    {
        "id": "curated_zara_01",
        "brand": "Zara Canada",
        "brand_key": "zara",
        "title": "Baby Girl Knit Ruffled Sweater Dress - Dusty Rose",
        "price_cad": 22.90,
        "original_price_cad": 45.90,
        "discount_pct": 50.1,
        "savings_cad": 23.00,
        "badge": "🔥 超级神价 (Steal)",
        "stars": "⭐⭐⭐⭐⭐",
        "value_tier": "ultra_high",
        "category": "clothes",
        "sizes": ["3-6M", "6-9M", "9-12M", "12-18M"],
        "in_stock": True,
        "product_url": "https://www.zara.com/ca/en/kids-babygirl-special-prices-l414.html",
        "image_url": "https://static.zara.net/stdstatic/6.19.0/images/zara-logo.svg",
        "source": "Zara Canada Special Prices",
        "collection": "Zara Baby Girl Deals"
    },
    {
        "id": "curated_hm_01",
        "brand": "H&M Canada",
        "brand_key": "hm",
        "title": "5-Pack Long-sleeve Organic Cotton Bodysuits (Floral & Pastel)",
        "price_cad": 17.99,
        "original_price_cad": 29.99,
        "discount_pct": 40.0,
        "savings_cad": 12.00,
        "badge": "🏷️ 高性价比 (Great Deal)",
        "stars": "⭐⭐⭐⭐",
        "value_tier": "high",
        "category": "clothes",
        "sizes": ["1-2M", "2-4M", "4-6M", "6-9M", "9-12M"],
        "in_stock": True,
        "product_url": "https://www2.hm.com/en_ca/baby/sale/baby-girl.html",
        "image_url": "https://www2.hm.com/hm-logo.png",
        "source": "H&M Canada Official Sale",
        "collection": "H&M Baby Girl Deals"
    },
    {
        "id": "curated_carters_01",
        "brand": "Carter's OshKosh Canada",
        "brand_key": "carters",
        "title": "Baby Girl 2-Piece Holiday Fleece Top & Legging Set",
        "price_cad": 11.99,
        "original_price_cad": 26.00,
        "discount_pct": 53.9,
        "savings_cad": 14.01,
        "badge": "🔥 超级神价 (Steal)",
        "stars": "⭐⭐⭐⭐⭐",
        "value_tier": "ultra_high",
        "category": "clothes",
        "sizes": ["3M", "6M", "9M", "12M", "18M", "24M"],
        "in_stock": True,
        "product_url": "https://www.cartersoshkosh.ca/en_CA/carters-baby-girl-clearance",
        "image_url": "https://www.cartersoshkosh.ca/on/demandware.static/-/Sites-Carters-Library/default/dw1d9f8266/images/carters-logo.svg",
        "source": "Carter's Canada Doorbusters",
        "collection": "Carter's Canada Official"
    }
]

def get_curated_deals() -> List[Dict]:
    return CURATED_HOT_DEALS

def get_brand_shopping_guides() -> List[Dict]:
    return CURATED_BRAND_GUIDES
