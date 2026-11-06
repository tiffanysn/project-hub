#!/usr/bin/env python3
"""
Main Entry Point: Canada Baby Girl Deals & Holiday Discounts Aggregator
"""

import argparse
import csv
import json
import os
import sys

# Ensure current directory is in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from config import (
    DEFAULT_POSTAL_CODE,
    MIN_DISCOUNT_PERCENT,
    OUTPUT_CSV,
    OUTPUT_HTML,
    OUTPUT_JSON,
    DATA_DIR
)
from scrapers.shopify_scraper import ShopifyScraper
from scrapers.flipp_scraper import FlippCanadaScraper
from scrapers.curated_brand_deals import get_curated_deals
from reporters.html_reporter import generate_html_dashboard

def save_csv(deals: list, path: str):
    """Saves deals list to CSV file."""
    if not deals:
        return
    fieldnames = [
        "brand", "title", "category", "price_cad", "original_price_cad",
        "discount_pct", "savings_cad", "badge", "stars", "sizes",
        "product_url", "source"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for d in deals:
            row = d.copy()
            if isinstance(row.get("sizes"), list):
                row["sizes"] = ", ".join(row["sizes"])
            writer.writerow(row)

def save_json(deals: list, path: str):
    """Saves deals list to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(deals, f, ensure_ascii=False, indent=2)

def print_terminal_summary(deals: list):
    """Prints a structured summary table in the terminal."""
    print("\n" + "=" * 80)
    print("🍁 加拿大黑五 & 12月女宝宝精选折扣大促汇总")
    print("=" * 80)

    if not deals:
        print("未找到符合条件的折扣商品。")
        return

    # Print top 12 highlight deals
    print(f"{'品牌':<20} | {'品类':<6} | {'现价(CAD)':<10} | {'原价':<8} | {'折扣':<7} | {'评级与商品名称'}")
    print("-" * 80)

    for d in deals[:15]:
        brand = d.get("brand", "")[:18]
        cat = {"clothes": "衣服", "shoes": "鞋靴", "toys": "玩具", "home": "家居"}.get(d.get("category"), "母婴")
        price = f"${d.get('price_cad', 0):.2f}"
        orig = f"${d.get('original_price_cad', 0):.2f}"
        disc = f"-{d.get('discount_pct', 0):.0f}%"
        badge = d.get("badge", "").split(" ")[0]
        title = d.get("title", "")[:28]
        print(f"{brand:<20} | {cat:<6} | {price:<10} | {orig:<8} | {disc:<7} | {badge} {title}")

    print("-" * 80)
    avg_disc = sum(d.get("discount_pct", 0) for d in deals) / len(deals)
    steals = sum(1 for d in deals if d.get("discount_pct", 0) >= 50 or d.get("price_cad", 0) <= 15)
    print(f"📊 汇总统计: 共收录 {len(deals)} 件商品 | 平均折扣 -{avg_disc:.1f}% | 包含 {steals} 款超值神价好物")
    print(f"📁 数据导出路径: {OUTPUT_HTML}")
    print("=" * 80 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Canada Baby Girl Holiday Deals Scraper")
    parser.add_argument("--brand", choices=["all", "dpd", "stonz", "konny", "flipp", "curated"], default="all",
                        help="Scrape specific brand or 'all'")
    parser.add_argument("--category", choices=["all", "clothes", "shoes", "toys", "home"], default="all",
                        help="Filter by specific category")
    parser.add_argument("--min-discount", type=float, default=MIN_DISCOUNT_PERCENT,
                        help=f"Minimum discount percentage (default: {MIN_DISCOUNT_PERCENT}%%)")
    parser.add_argument("--postal-code", default=DEFAULT_POSTAL_CODE,
                        help=f"Canadian Postal Code for store flyers (default: {DEFAULT_POSTAL_CODE})")

    args = parser.parse_args()

    os.makedirs(DATA_DIR, exist_ok=True)
    all_deals = []

    print(f"\n🚀 开始抓取加拿大黑五 & 12月女宝宝折扣数据 (最低折扣要求: {args.min_discount}%)...")

    # 1. Shopify stores (DPD, Stonz, Konny)
    if args.brand in ["all", "dpd", "stonz", "konny"]:
        shopify_scraper = ShopifyScraper()
        if args.brand == "all":
            print("  ⏳ 正在拉取 Stonz / Deux par Deux / Konny 官方实时清仓数据...")
            shopify_deals = shopify_scraper.scrape_all(min_discount=args.min_discount)
        else:
            brand_map = {"dpd": "deuxpardeux", "stonz": "stonz", "konny": "konny"}
            shopify_deals = shopify_scraper.scrape_store(brand_map[args.brand], min_discount=args.min_discount)
        all_deals.extend(shopify_deals)
        print(f"  ✅ 官方独立站抓取完成: 获取 {len(shopify_deals)} 件实时好价！")

    # 2. Flipp Canada (Carter's, Walmart, Toys R Us)
    if args.brand in ["all", "flipp"]:
        print(f"  ⏳ 正在检索加拿大全境零售商促销与海报 (邮编: {args.postal_code})...")
        flipp_scraper = FlippCanadaScraper(postal_code=args.postal_code)
        flipp_deals = flipp_scraper.scrape_all(min_discount=args.min_discount)
        all_deals.extend(flipp_deals)
        print(f"  ✅ 零售商与海报抓取完成: 获取 {len(flipp_deals)} 件折扣好物！")

    # 3. Curated Black Friday & Brand Specials (Gap, Zara, H&M, Carter's)
    if args.brand in ["all", "curated"]:
        curated_deals = get_curated_deals()
        all_deals.extend(curated_deals)

    # Filter by category if specified
    if args.category != "all":
        all_deals = [d for d in all_deals if d.get("category") == args.category]

    # Deduplicate and sort by discount percentage descending
    unique_deals = []
    seen_ids = set()
    for d in all_deals:
        did = d.get("id") or d.get("title")
        if did not in seen_ids:
            unique_deals.append(d)
            seen_ids.add(did)

    unique_deals.sort(key=lambda x: x.get("discount_pct", 0), reverse=True)

    # Save outputs
    save_json(unique_deals, OUTPUT_JSON)
    save_csv(unique_deals, OUTPUT_CSV)
    generate_html_dashboard(unique_deals, OUTPUT_HTML)

    # Terminal presentation
    print_terminal_summary(unique_deals)
    print(f"💡 提示：可以在浏览器中直接打开可视化看板：\nopen {OUTPUT_HTML}\n")

if __name__ == "__main__":
    main()
