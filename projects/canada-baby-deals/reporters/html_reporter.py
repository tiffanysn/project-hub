"""
HTML Visual Dashboard Generator for Canada Baby Girl Deals
Generates a standalone, interactive, responsive web report for browsing deals.
"""

import json
import os
from typing import List, Dict
from scrapers.curated_brand_deals import get_brand_shopping_guides

def generate_html_dashboard(deals: List[Dict], output_path: str):
    """Generates an interactive, beautiful HTML deals dashboard."""

    # Compute key statistics
    total_count = len(deals)
    if total_count > 0:
        avg_discount = round(sum(d.get("discount_pct", 0) for d in deals) / total_count, 1)
        max_discount = max(d.get("discount_pct", 0) for d in deals)
        avg_price = round(sum(d.get("price_cad", 0) for d in deals) / total_count, 2)
        steal_count = sum(1 for d in deals if d.get("discount_pct", 0) >= 50 or d.get("price_cad", 0) <= 15)
    else:
        avg_discount = max_discount = avg_price = steal_count = 0

    brand_guides = get_brand_shopping_guides()
    deals_json = json.dumps(deals, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🍁 加拿大黑五 & 12月女宝宝精选折扣大促看板</title>
    <style>
        :root {{
            --primary: #f06292;
            --primary-dark: #d81b60;
            --primary-light: #fce4ec;
            --accent: #ff80ab;
            --bg: #f8f9fa;
            --card-bg: #ffffff;
            --text-main: #2d3748;
            --text-sub: #718096;
            --border: #edf2f7;
            --shadow: 0 4px 12px rgba(0,0,0,0.06);
            --radius: 12px;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: var(--bg);
            color: var(--text-main);
            line-height: 1.6;
            padding: 24px 16px 60px;
        }}
        .container {{
            max-width: 1280px;
            margin: 0 auto;
        }}
        /* Header */
        header {{
            background: linear-gradient(135deg, #fce4ec 0%, #fff 100%);
            border-radius: var(--radius);
            padding: 28px 24px;
            border: 1px solid #f8bbd0;
            margin-bottom: 24px;
            box-shadow: var(--shadow);
        }}
        header h1 {{
            font-size: 26px;
            color: var(--primary-dark);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        header p {{
            color: var(--text-sub);
            font-size: 14px;
        }}
        /* Stats Grid */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }}
        .stat-card {{
            background: var(--card-bg);
            padding: 18px 20px;
            border-radius: var(--radius);
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            text-align: center;
        }}
        .stat-label {{
            font-size: 13px;
            color: var(--text-sub);
            margin-bottom: 6px;
        }}
        .stat-value {{
            font-size: 26px;
            font-weight: 700;
            color: var(--primary-dark);
        }}
        /* Brand Guides */
        .guides-section {{
            background: var(--card-bg);
            border-radius: var(--radius);
            padding: 20px;
            border: 1px solid var(--border);
            margin-bottom: 24px;
            box-shadow: var(--shadow);
        }}
        .guides-title {{
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 14px;
            color: var(--text-main);
        }}
        .guides-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 14px;
        }}
        .guide-box {{
            background: #fff0f5;
            padding: 14px 16px;
            border-radius: 8px;
            border-left: 4px solid var(--primary);
            font-size: 13px;
        }}
        .guide-box h4 {{
            color: var(--primary-dark);
            margin-bottom: 4px;
            display: flex;
            justify-content: space-between;
        }}
        .guide-box a {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
        }}
        /* Control Bar */
        .controls {{
            background: var(--card-bg);
            border-radius: var(--radius);
            padding: 18px 20px;
            border: 1px solid var(--border);
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            align-items: center;
            justify-content: space-between;
        }}
        .filter-group {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        .btn-filter {{
            background: #fff;
            border: 1px solid #cbd5e0;
            padding: 7px 14px;
            border-radius: 20px;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .btn-filter:hover {{
            border-color: var(--primary);
            color: var(--primary);
        }}
        .btn-filter.active {{
            background: var(--primary);
            border-color: var(--primary);
            color: #fff;
            font-weight: 600;
        }}
        .search-input {{
            padding: 8px 16px;
            border: 1px solid #cbd5e0;
            border-radius: 20px;
            font-size: 13px;
            width: 240px;
            outline: none;
        }}
        .search-input:focus {{
            border-color: var(--primary);
        }}
        /* Deals Grid */
        .deals-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }}
        .deal-card {{
            background: var(--card-bg);
            border-radius: var(--radius);
            border: 1px solid var(--border);
            overflow: hidden;
            box-shadow: var(--shadow);
            display: flex;
            flex-direction: column;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            position: relative;
        }}
        .deal-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }}
        .img-container {{
            width: 100%;
            height: 220px;
            background: #fff5f8;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }}
        .img-container img {{
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
            transition: transform 0.3s;
        }}
        .deal-card:hover .img-container img {{
            transform: scale(1.05);
        }}
        .discount-badge {{
            position: absolute;
            top: 12px;
            right: 12px;
            background: #e53e3e;
            color: #fff;
            font-weight: 700;
            font-size: 13px;
            padding: 4px 9px;
            border-radius: 14px;
            box-shadow: 0 2px 6px rgba(229, 62, 62, 0.4);
        }}
        .category-badge {{
            position: absolute;
            top: 12px;
            left: 12px;
            background: rgba(255, 255, 255, 0.9);
            color: #4a5568;
            font-size: 11px;
            font-weight: 600;
            padding: 3px 8px;
            border-radius: 8px;
            backdrop-filter: blur(4px);
        }}
        .card-body {{
            padding: 16px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}
        .brand-name {{
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--primary-dark);
            margin-bottom: 4px;
        }}
        .product-title {{
            font-size: 14px;
            font-weight: 600;
            color: #1a202c;
            margin-bottom: 10px;
            line-height: 1.4;
            height: 40px;
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
        }}
        .price-section {{
            display: flex;
            align-items: baseline;
            gap: 8px;
            margin-bottom: 8px;
        }}
        .current-price {{
            font-size: 20px;
            font-weight: 700;
            color: #e53e3e;
        }}
        .original-price {{
            font-size: 13px;
            color: #a0aec0;
            text-decoration: line-through;
        }}
        .savings-tag {{
            font-size: 11px;
            color: #38a169;
            font-weight: 600;
        }}
        .value-badge {{
            font-size: 12px;
            margin-bottom: 12px;
            color: #4a5568;
        }}
        .sizes-row {{
            font-size: 11px;
            color: #718096;
            margin-bottom: 12px;
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
        }}
        .size-tag {{
            background: #edf2f7;
            padding: 2px 6px;
            border-radius: 4px;
        }}
        .btn-buy {{
            margin-top: auto;
            display: block;
            text-align: center;
            background: var(--primary);
            color: #fff;
            padding: 9px 12px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 600;
            transition: background 0.2s ease;
        }}
        .btn-buy:hover {{
            background: var(--primary-dark);
        }}
        .empty-state {{
            grid-column: 1 / -1;
            text-align: center;
            padding: 60px 20px;
            color: var(--text-sub);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🍁 加拿大黑五 & 12月女宝宝折扣特惠看板</h1>
            <p>专注于高性价比女宝宝好物（0-24M / 幼童），覆盖衣服、雪服、鞋子、温哥华/多伦多过冬装备、玩具及家居用品。货币：加币 (CAD)。</p>
        </header>

        <!-- Stats -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">收录折扣商品</div>
                <div class="stat-value">{total_count} 件</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">平均折扣幅度</div>
                <div class="stat-value">-{avg_discount}%</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">最高单品折扣</div>
                <div class="stat-value">-{max_discount}%</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">🔥 超级神价好物</div>
                <div class="stat-value">{steal_count} 款</div>
            </div>
        </div>

        <!-- Brand Strategy Guides -->
        <div class="guides-section">
            <div class="guides-title">🛍️ 加拿大热门品牌黑五 & 12月大促抢购攻略</div>
            <div class="guides-grid">"""

    for g in brand_guides:
        html_content += f"""
                <div class="guide-box">
                    <h4>{g['brand']} <a href="{g['official_url']}" target="_blank">官网专区 ↗</a></h4>
                    <p><strong>折扣策略：</strong>{g['bf_strategy']}</p>
                    <p><strong>推荐必入：</strong>{g['best_picks']}</p>
                </div>"""

    html_content += f"""
            </div>
        </div>

        <!-- Controls -->
        <div class="controls">
            <div class="filter-group" id="category-filters">
                <button class="btn-filter active" data-cat="all">全部品类</button>
                <button class="btn-filter" data-cat="clothes">👗 衣服 & 雪服</button>
                <button class="btn-filter" data-cat="shoes">👟 鞋子 & 雪靴</button>
                <button class="btn-filter" data-cat="toys">🧸 益智玩具</button>
                <button class="btn-filter" data-cat="home">🏡 家居 & 睡袋</button>
            </div>
            <div class="filter-group" id="tier-filters">
                <button class="btn-filter active" data-tier="all">全部折扣</button>
                <button class="btn-filter" data-tier="steal">🔥 5折+ 超级神价</button>
                <button class="btn-filter" data-tier="budget">💰 $20加币以下白菜价</button>
            </div>
            <input type="text" id="search-input" class="search-input" placeholder="🔍 搜索品牌、商品或款式...">
        </div>

        <!-- Deals Grid -->
        <div class="deals-grid" id="deals-container"></div>
    </div>

    <script>
        const allDeals = {deals_json};
        let currentCat = "all";
        let currentTier = "all";
        let searchQuery = "";

        const categoryNames = {{
            "clothes": "👗 衣服",
            "shoes": "👟 鞋靴",
            "toys": "🧸 玩具",
            "home": "🏡 家居"
        }};

        function renderDeals() {{
            const container = document.getElementById("deals-container");
            container.innerHTML = "";

            const filtered = allDeals.filter(d => {{
                // Category filter
                if (currentCat !== "all" && d.category !== currentCat) return false;

                // Tier filter
                if (currentTier === "steal" && (d.discount_pct < 50 && d.price_cad > 15)) return false;
                if (currentTier === "budget" && d.price_cad > 20) return false;

                // Search query
                if (searchQuery) {{
                    const q = searchQuery.toLowerCase();
                    const text = (d.title + " " + d.brand + " " + (d.category || "")).toLowerCase();
                    if (!text.includes(q)) return false;
                }}
                return true;
            }});

            if (filtered.length === 0) {{
                container.innerHTML = '<div class="empty-state"><h3>暂无匹配的折扣商品</h3><p>请尝试更换品类或清除搜索关键词。</p></div>';
                return;
            }}

            filtered.forEach(d => {{
                const card = document.createElement("div");
                card.className = "deal-card";

                const fallbackImg = "https://images.unsplash.com/photo-1519689680058-324335c77eba?w=400";
                const imgUrl = d.image_url || fallbackImg;
                const catLabel = categoryNames[d.category] || "👶 母婴";

                const sizeHtml = (d.sizes && d.sizes.length > 0)
                    ? '<div class="sizes-row">' + d.sizes.map(s => `<span class="size-tag">${{s}}</span>`).join("") + '</div>'
                    : '';

                card.innerHTML = `
                    <div class="img-container">
                        <span class="category-badge">${{catLabel}}</span>
                        <span class="discount-badge">-${{Math.round(d.discount_pct)}}%</span>
                        <img src="${{imgUrl}}" alt="${{d.title}}" onerror="this.src='${{fallbackImg}}'">
                    </div>
                    <div class="card-body">
                        <div class="brand-name">${{d.brand}}</div>
                        <div class="product-title" title="${{d.title}}">${{d.title}}</div>
                        <div class="price-section">
                            <span class="current-price">$${{d.price_cad.toFixed(2)}} CAD</span>
                            <span class="original-price">$${{d.original_price_cad.toFixed(2)}}</span>
                            <span class="savings-tag">省 $${{d.savings_cad.toFixed(2)}}</span>
                        </div>
                        <div class="value-badge">${{d.badge}} ${{d.stars || ''}}</div>
                        ${{sizeHtml}}
                        <a href="${{d.product_url}}" target="_blank" class="btn-buy">前往查看直达 ↗</a>
                    </div>
                `;
                container.appendChild(card);
            }});
        }}

        // Event listeners
        document.querySelectorAll("#category-filters .btn-filter").forEach(btn => {{
            btn.addEventListener("click", () => {{
                document.querySelectorAll("#category-filters .btn-filter").forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                currentCat = btn.dataset.cat;
                renderDeals();
            }});
        }});

        document.querySelectorAll("#tier-filters .btn-filter").forEach(btn => {{
            btn.addEventListener("click", () => {{
                document.querySelectorAll("#tier-filters .btn-filter").forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                currentTier = btn.dataset.tier;
                renderDeals();
            }});
        }});

        document.getElementById("search-input").addEventListener("input", (e) => {{
            searchQuery = e.target.value.trim();
            renderDeals();
        }});

        // Initial render
        renderDeals();
    </script>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
