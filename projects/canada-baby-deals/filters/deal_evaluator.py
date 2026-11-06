"""
Deal Evaluator & Filter for Baby Girl Items and Cost-Performance Scoring
"""

import re
from config import CATEGORY_KEYWORDS

# Negative keywords for baby girl (exclude explicit boy-only items)
BOY_EXCLUSIVE_KEYWORDS = [
    r"\bboy\b", r"\bboys\b", r"\bboy\'s\b", r"\bboys\'\b",
    r"\bdinosaur\b", r"\bt-rex\b", r"\btractor\b", r"\btruck\b"
]

# Positive keywords for girl / feminine aesthetics
GIRL_POSITIVE_KEYWORDS = [
    r"\bgirl\b", r"\bgirls\b", r"\bgirl\'s\b", r"\bgirls\'\b",
    r"\bpink\b", r"\bfloral\b", r"\bflower\b", r"\brose\b",
    r"\bdress\b", r"\bskirt\b", r"\btutu\b", r"\bheadband\b",
    r"\bheart\b", r"\bglitter\b", r"\blace\b", r"\bruffle\b",
    r"\bbutterfly\b", r"\bballet\b", r"\bbow\b"
]

# Neutral / Essential keywords (keep unless boy-exclusive)
NEUTRAL_KEYWORDS = [
    r"\bbaby\b", r"\bnewborn\b", r"\binfant\b", r"\btoddler\b",
    r"\bunisex\b", r"\bbootie\b", r"\bboot\b", r"\bmitt\b",
    r"\bblanket\b", r"\bbib\b", r"\bcarrier\b", r"\bsnowsuit\b"
]

def is_baby_girl_relevant(title: str, description: str = "", tags: list = None) -> bool:
    """
    Determines if an item is appropriate for a baby girl.
    Returns True if:
    - Explicitly marked girl, OR
    - Neutral/unisex with no boy-exclusive markers, OR
    - Features feminine patterns/colors.
    """
    text = f"{title} {description} {' '.join(tags or [])}".lower()

    # If it explicitly mentions baby boy / boys, exclude unless it says 'baby boy and girl'
    for pattern in BOY_EXCLUSIVE_KEYWORDS:
        if re.search(pattern, text):
            # Check if it also mentions girl or unisex
            if not re.search(r"\bgirl\b|\bunisex\b", text):
                return False

    # Check for positive girl indicator or neutral/baby indicator
    has_girl = any(re.search(p, text) for p in GIRL_POSITIVE_KEYWORDS)
    has_neutral = any(re.search(p, text) for p in NEUTRAL_KEYWORDS)

    return has_girl or has_neutral

def detect_category(title: str, default_cat: str = "clothes") -> str:
    """
    Detects product category: clothes, shoes, toys, home
    """
    title_lower = title.lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in title_lower for kw in keywords):
            return cat
    return default_cat

def score_deal(price: float, original_price: float, brand: str) -> dict:
    """
    Calculates discount and value-for-money score (高性价比打分)
    """
    if not original_price or original_price <= price or original_price <= 0:
        discount_pct = 0.0
    else:
        discount_pct = round((1.0 - (price / original_price)) * 100, 1)

    # Cost-performance badge & stars
    if discount_pct >= 50 or (discount_pct >= 30 and price <= 15.0):
        badge = "🔥 超级神价 (Steal)"
        stars = "⭐⭐⭐⭐⭐"
        value_tier = "ultra_high"
    elif discount_pct >= 35 or (discount_pct >= 20 and price <= 25.0):
        badge = "🏷️ 高性价比 (Great Deal)"
        stars = "⭐⭐⭐⭐"
        value_tier = "high"
    elif discount_pct >= 20:
        badge = "✨ 限时好折 (Good Value)"
        stars = "⭐⭐⭐"
        value_tier = "medium"
    else:
        badge = "💡 平价日常 (Regular)"
        stars = "⭐⭐"
        value_tier = "standard"

    savings = round(max(0.0, original_price - price), 2) if original_price else 0.0

    return {
        "discount_pct": discount_pct,
        "savings_cad": savings,
        "badge": badge,
        "stars": stars,
        "value_tier": value_tier
    }
