"""
Configuration for Canada Baby Girl Deals Crawler (Black Friday & Holiday Season)
"""

import os

# Default Canadian settings
DEFAULT_POSTAL_CODE = "M5V2T6"  # Toronto / Ontario (representative for Canada-wide shipping)
CURRENCY = "CAD"
MIN_DISCOUNT_PERCENT = 20  # Minimum discount to consider as a deal
HIGH_VALUE_DISCOUNT = 40   # Threshold for "Super Value" (高性价比) tag

# Category keywords mapping
CATEGORY_KEYWORDS = {
    "shoes": [
        "boot", "bootie", "shoe", "slipper", "mitt", "footwear", 
        "pre-walker", "sneaker", "sandal", "rain-boot", "winter-boot"
    ],
    "clothes": [
        "dress", "bodysuit", "romper", "onesie", "pajama", "sleepwear", 
        "snowsuit", "jacket", "coat", "sweater", "hoodie", "cardigan", 
        "pant", "legging", "short", "top", "t-shirt", "headband", 
        "hat", "overalls", "one-piece", "two-piece", "suit", "cotton"
    ],
    "toys": [
        "toy", "rattle", "teether", "plush", "doll", "puzzle", "block", 
        "sensory", "activity", "play", "stacker", "music", "ball"
    ],
    "home": [
        "blanket", "bib", "carrier", "sling", "sleep sack", "swaddle", 
        "crib", "nursery", "cocoon", "towel", "mat", "pillow", "bath", "wrap"
    ]
}

# Shopify-based Canadian Stores (Direct API access, 100% reliable)
SHOPIFY_STORES = {
    "deuxpardeux": {
        "name": "Deux par Deux (DPD)",
        "base_url": "https://deuxpardeux.com",
        "currency": "CAD",
        "description": "Quebec designer brand renowned for high-end winter snowsuits & durable, adorable baby girl wear.",
        "collections": [
            {"handle": "baby-girl-clearance", "category": "clothes", "name": "Baby Girl Clearance (清仓折扣)"},
            {"handle": "baby-girl-boots", "category": "shoes", "name": "Baby Girl Winter Boots & Footwear"},
            {"handle": "baby-girl-accessories", "category": "clothes", "name": "Baby Girl Accessories & Hats"},
            {"handle": "baby-girl-blankets", "category": "home", "name": "Baby Cocoon & Blankets"},
            {"handle": "baby-snowsuits", "category": "clothes", "name": "Baby & Toddler Snowsuits"},
            {"handle": "a-girl-her-dress", "category": "clothes", "name": "Girl Dresses & Outfits"}
        ]
    },
    "stonz": {
        "name": "Stonz Wear",
        "base_url": "https://stonz.com",
        "currency": "CAD",
        "description": "Top Canadian brand famous for winter baby booties, waterproof mitts, and first-step shoes.",
        "collections": [
            {"handle": "sale-clearance", "category": "shoes", "name": "Stonz Seasonal Sale & Clearance"},
            {"handle": "baby-mitts-and-booties", "category": "shoes", "name": "Baby Mitts & Warm Booties"},
            {"handle": "all-baby-shoes", "category": "shoes", "name": "All Baby Shoes"},
            {"handle": "winter-boots", "category": "shoes", "name": "Baby & Toddler Winter Boots"}
        ]
    },
    "konny": {
        "name": "Konny Baby",
        "base_url": "https://konnybaby.com",
        "currency": "CAD",
        "description": "Beloved ergonomic baby carriers, ultra-soft rolling bibs, and seasonal winter baby essentials.",
        "collections": [
            {"handle": "end-of-season-sale", "category": "clothes", "name": "Konny End of Season Sale"},
            {"handle": "flash-sale", "category": "clothes", "name": "Konny Flash Sale"},
            {"handle": "baby-bibs", "category": "home", "name": "Konny Rolling Bibs Collection"},
            {"handle": "bundle-up-collection", "category": "clothes", "name": "Bundle Up Winter Collection"},
            {"handle": "newborn-sale", "category": "clothes", "name": "Newborn Essentials Sale"}
        ]
    },
    "louloulollipop": {
        "name": "Loulou Lollipop (Vancouver)",
        "base_url": "https://louloulollipop.ca",
        "currency": "CAD",
        "description": "Vancouver designer baby brand famous for bamboo & TENCEL sleep bags, silicone teethers, and nursery gifts.",
        "collections": [
            {"handle": "sale", "category": "home", "name": "Loulou Lollipop Official Sale (特惠专区)"},
            {"handle": "0-5-tog-sleep-bags", "category": "home", "name": "0.5 TOG Baby Sleep Bags (四季透气睡袋)"},
            {"handle": "2-5-tog-sleep-bags", "category": "home", "name": "2.5 TOG Winter Warm Sleep Bags (秋冬加厚睡袋)"},
            {"handle": "teethers", "category": "toys", "name": "Baby Silicone Teethers & Toys (婴儿牙胶玩具)"}
        ]
    }
}

# Flipp Search Queries for Canadian Retailers & Flyers (Carter's, TCP, Walmart, Toys R Us, etc.)
FLIPP_SEARCHES = [
    {"query": "carters baby girl", "category": "clothes", "brand": "Carter's"},
    {"query": "carters baby outfit", "category": "clothes", "brand": "Carter's"},
    {"query": "the childrens place baby", "category": "clothes", "brand": "The Children's Place"},
    {"query": "childrens place baby girl", "category": "clothes", "brand": "The Children's Place"},
    {"query": "joe fresh baby girl", "category": "clothes", "brand": "Joe Fresh"},
    {"query": "old navy baby girl", "category": "clothes", "brand": "Old Navy"},
    {"query": "baby girl winter boots", "category": "shoes", "brand": "Multi-Brand"},
    {"query": "baby girl toys", "category": "toys", "brand": "Toys R Us / Multi"},
    {"query": "baby nursery", "category": "home", "brand": "Multi-Brand"},
    {"query": "gap baby girl", "category": "clothes", "brand": "Gap"}
]

# Output file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_JSON = os.path.join(DATA_DIR, "deals.json")
OUTPUT_CSV = os.path.join(DATA_DIR, "deals.csv")
OUTPUT_HTML = os.path.join(DATA_DIR, "deals_dashboard.html")
