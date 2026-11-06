"""
Curated Brand Deals & Black Friday / December Promotional Strategies for Canada
Covers: H&M, The Children's Place, Uniqlo, Nest Designs, Gap, Old Navy, Zara, Carter's, Joe Fresh, Loulou Lollipop.
"""

from typing import List, Dict

CURATED_BRAND_GUIDES = [
    {
        "brand": "The Children's Place (TCP)",
        "official_url": "https://www.childrensplace.com/ca-en/c/baby-girl-clothes",
        "sale_section_name": "TCP Canada Baby Girl Clearance",
        "bf_strategy": "加拿大平价性价比之王！黑五全场 50%~70% OFF + 全场包邮。大量 $4.99~$9.99 CAD 爆款抢购，摇粒绒睡衣与节日装极具性价比",
        "best_picks": "摇粒绒连体睡衣 (Microfleece Sleep & Play)、节日红格纹连衣裙、纯棉打底裤多件装"
    },
    {
        "brand": "优衣库 (Uniqlo Canada)",
        "official_url": "https://www.uniqlo.com/ca/en/baby",
        "sale_section_name": "Uniqlo Baby Girl Special Offers",
        "bf_strategy": "11月感恩节 Arigato Festival 与黑五大促，婴儿 Heattech 吸湿发热打底衣、摇粒绒家居服直降，网店限时满额免邮",
        "best_picks": "Heattech 棉质连体打底衣 (发热包屁衣)、摇粒绒家居睡衣、可水洗空气保暖棉服 (Warm Padded Parka)"
    },
    {
        "brand": "Nest Designs (温哥华高端母婴)",
        "official_url": "https://www.nestdesigns.com/collections/baby-sleepwear",
        "sale_section_name": "Nest Designs Canadian Sale & Clearance",
        "bf_strategy": "温哥华本土高端竹纤维品牌！黑五全场 20%~40% OFF，断码清仓区低至 5 折。手感极细腻软糯",
        "best_picks": "0.5 / 1.0 / 2.5 TOG 恒温竹纤维睡袋、分腿睡袋 (Sleep Suit)、双向拉链包脚连体衣 (Footie)、双面纱布被"
    },
    {
        "brand": "H&M Canada",
        "official_url": "https://www2.hm.com/en_ca/baby/sale/baby-girl.html",
        "sale_section_name": "H&M Baby Girl Sale",
        "bf_strategy": "免费会员黑五全场 25%~30% OFF 免运费；12月节前每日特惠 (Holiday Countdown) 及年末 Boxing Day 折上折低至 3 折",
        "best_picks": "纯棉多件装长袖包屁衣、荷叶边针织连衣裙、加厚羊羔绒保暖外套、婴儿软底学步鞋"
    },
    {
        "brand": "Carter's OshKosh Canada",
        "official_url": "https://www.cartersoshkosh.ca/en_CA/carters-baby-girl-clearance",
        "sale_section_name": "Carter's Canada Official Baby Girl Clearance",
        "bf_strategy": "黑五全场 50%~60% OFF + 门票爆款 (Doorbusters $5~$9 CAD) + 全场无门槛包邮，12月双旦折上折",
        "best_picks": "纯棉双向拉链睡袋 (Sleep & Play)、节日红/格纹连体裙、加绒两件套、保暖棉坎肩"
    },
    {
        "brand": "Gap Canada & Old Navy",
        "official_url": "https://www.gapcanada.ca/browse/category.do?cid=65217",
        "sale_section_name": "Gap & Old Navy Baby Girl Deals",
        "bf_strategy": "Gap 黑五全场 50% OFF + 额外 10% 折上折；Old Navy 更是 $5~$10 CAD 平价天花板，12月年终清仓低至 3 折",
        "best_picks": "有机棉连体衣 (Bodysuits)、小熊耳朵加绒连帽外套、摇粒绒卫裤、节日亲子家居服"
    },
    {
        "brand": "Zara Canada",
        "official_url": "https://www.zara.com/ca/en/kids-babygirl-special-prices-l414.html",
        "sale_section_name": "Zara Baby Girl Special Prices",
        "bf_strategy": "黑五精选 40% OFF（黑五前夕 8:00 PM App 抢先开抢）；12月25日 Boxing Day 开启全季大清仓（3-5折）",
        "best_picks": "设计款复古粉连衣裙、针织毛衣、复古软底学步鞋、羊羔绒保暖外套"
    },
    {
        "brand": "Joe Fresh (加拿大国民品牌)",
        "official_url": "https://www.joefresh.com/ca/Categories/Baby/Baby-Girl/c/10006",
        "sale_section_name": "Joe Fresh Baby Girl Clearance",
        "bf_strategy": "加拿大 Superstore / Loblaws 旗下平价之选！黑五全场 25%~40% OFF + 赠送海量 PC Optimum 积分，相当于额外折现",
        "best_picks": "轻薄保暖连体羽绒服 (Primaloft Snowsuit)、抓绒保暖爬服、纯棉日常打底裤组合"
    }
]

CURATED_HOT_DEALS = [
    # The Children's Place
    {
        "id": "curated_tcp_01",
        "brand": "The Children's Place",
        "brand_key": "tcp",
        "title": "Baby Girl Microfleece Zip-Up Sleep & Play Pajamas",
        "price_cad": 8.99,
        "original_price_cad": 22.95,
        "discount_pct": 60.8,
        "savings_cad": 13.96,
        "badge": "🔥 超级神价 (Steal)",
        "stars": "⭐⭐⭐⭐⭐",
        "value_tier": "ultra_high",
        "category": "clothes",
        "sizes": ["0-3M", "3-6M", "6-9M", "12M", "18M"],
        "in_stock": True,
        "product_url": "https://www.childrensplace.com/ca-en/c/baby-girl-clothes",
        "image_url": "https://www.childrensplace.com/static-assets/common/images/tcp-logo.svg",
        "source": "TCP Canada Official BF Sale",
        "collection": "The Children's Place Deals"
    },
    {
        "id": "curated_tcp_02",
        "brand": "The Children's Place",
        "brand_key": "tcp",
        "title": "Baby Girl Holiday Red Plaid Ruffle Dress & Bloomers Set",
        "price_cad": 14.99,
        "original_price_cad": 36.95,
        "discount_pct": 59.4,
        "savings_cad": 21.96,
        "badge": "🔥 超级神价 (Steal)",
        "stars": "⭐⭐⭐⭐⭐",
        "value_tier": "ultra_high",
        "category": "clothes",
        "sizes": ["3-6M", "6-9M", "12M", "18M", "24M"],
        "in_stock": True,
        "product_url": "https://www.childrensplace.com/ca-en/c/baby-girl-clothes",
        "image_url": "https://www.childrensplace.com/static-assets/common/images/tcp-logo.svg",
        "source": "TCP Canada Holiday Special",
        "collection": "The Children's Place Deals"
    },
    # Uniqlo Canada
    {
        "id": "curated_uniqlo_01",
        "brand": "优衣库 (Uniqlo Canada)",
        "brand_key": "uniqlo",
        "title": "Baby Girl Heattech Cotton Long-Sleeve Bodysuit (2-Pack)",
        "price_cad": 14.90,
        "original_price_cad": 24.90,
        "discount_pct": 40.2,
        "savings_cad": 10.00,
        "badge": "🏷️ 高性价比 (Great Deal)",
        "stars": "⭐⭐⭐⭐⭐",
        "value_tier": "high",
        "category": "clothes",
        "sizes": ["3-6M (60)", "6-12M (70)", "12-18M (80)", "18-24M (90)"],
        "in_stock": True,
        "product_url": "https://www.uniqlo.com/ca/en/baby",
        "image_url": "https://www.uniqlo.com/ca/en/static/images/logo.svg",
        "source": "Uniqlo Canada Arigato Festival",
        "collection": "Uniqlo Baby Special"
    },
    {
        "id": "curated_uniqlo_02",
        "brand": "优衣库 (Uniqlo Canada)",
        "brand_key": "uniqlo",
        "title": "Baby Fluffy Yarn Fleece One-Piece Pajamas (Pastel Pink)",
        "price_cad": 19.90,
        "original_price_cad": 29.90,
        "discount_pct": 33.4,
        "savings_cad": 10.00,
        "badge": "🏷️ 高性价比 (Great Deal)",
        "stars": "⭐⭐⭐⭐",
        "value_tier": "high",
        "category": "clothes",
        "sizes": ["6-12M (70)", "12-18M (80)", "18-24M (90)", "2-3Y (100)"],
        "in_stock": True,
        "product_url": "https://www.uniqlo.com/ca/en/baby",
        "image_url": "https://www.uniqlo.com/ca/en/static/images/logo.svg",
        "source": "Uniqlo Canada Black Friday",
        "collection": "Uniqlo Baby Special"
    },
    # Nest Designs
    {
        "id": "curated_nest_01",
        "brand": "Nest Designs (温哥华)",
        "brand_key": "nest",
        "title": "Bamboo Silk Dual-Zip Baby Sleep Bag 1.0 TOG - Secret Garden",
        "price_cad": 44.80,
        "original_price_cad": 64.00,
        "discount_pct": 30.0,
        "savings_cad": 19.20,
        "badge": "✨ 限时好折 (Good Value)",
        "stars": "⭐⭐⭐⭐⭐",
        "value_tier": "medium",
        "category": "home",
        "sizes": ["0-6M", "6-18M", "18-36M"],
        "in_stock": True,
        "product_url": "https://www.nestdesigns.com/collections/baby-sleepwear",
        "image_url": "https://www.nestdesigns.com/images/logo.svg",
        "source": "Nest Designs Official Holiday Sale",
        "collection": "Nest Designs Sleepwear"
    },
    {
        "id": "curated_nest_02",
        "brand": "Nest Designs (温哥华)",
        "brand_key": "nest",
        "title": "Organic Cotton Ribbed Footie Romper - Vintage Rose",
        "price_cad": 27.30,
        "original_price_cad": 39.00,
        "discount_pct": 30.0,
        "savings_cad": 11.70,
        "badge": "✨ 限时好折 (Good Value)",
        "stars": "⭐⭐⭐⭐",
        "value_tier": "medium",
        "category": "clothes",
        "sizes": ["NB", "0-3M", "3-6M", "6-12M"],
        "in_stock": True,
        "product_url": "https://www.nestdesigns.com/collections/baby-sleepwear",
        "image_url": "https://www.nestdesigns.com/images/logo.svg",
        "source": "Nest Designs Holiday Clearance",
        "collection": "Nest Designs Sleepwear"
    },
    # H&M Canada
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
        "id": "curated_hm_02",
        "brand": "H&M Canada",
        "brand_key": "hm",
        "title": "Baby Girl Fluffy Padded Winter Overall Suit with Ears",
        "price_cad": 29.99,
        "original_price_cad": 49.99,
        "discount_pct": 40.0,
        "savings_cad": 20.00,
        "badge": "🏷️ 高性价比 (Great Deal)",
        "stars": "⭐⭐⭐⭐",
        "value_tier": "high",
        "category": "clothes",
        "sizes": ["2-4M", "4-6M", "6-9M", "9-12M"],
        "in_stock": True,
        "product_url": "https://www2.hm.com/en_ca/baby/sale/baby-girl.html",
        "image_url": "https://www2.hm.com/hm-logo.png",
        "source": "H&M Canada Winter Outerwear Sale",
        "collection": "H&M Baby Girl Deals"
    },
    # Joe Fresh Canada
    {
        "id": "curated_joe_01",
        "brand": "Joe Fresh",
        "brand_key": "joefresh",
        "title": "Baby Girl Packable Primaloft Snowsuit / Puffer Suit",
        "price_cad": 29.00,
        "original_price_cad": 49.00,
        "discount_pct": 40.8,
        "savings_cad": 20.00,
        "badge": "🏷️ 高性价比 (Great Deal)",
        "stars": "⭐⭐⭐⭐",
        "value_tier": "high",
        "category": "clothes",
        "sizes": ["0-3M", "3-6M", "6-12M", "12-18M", "18-24M"],
        "in_stock": True,
        "product_url": "https://www.joefresh.com/ca/Categories/Baby/Baby-Girl/c/10006",
        "image_url": "https://www.joefresh.com/assets/images/logo.svg",
        "source": "Joe Fresh Holiday Sale",
        "collection": "Joe Fresh Baby Girl Deals"
    },
    # Old Navy Canada
    {
        "id": "curated_oldnavy_01",
        "brand": "Old Navy Canada",
        "brand_key": "oldnavy",
        "title": "Baby Girl Cozy Sherpa-Lined Full-Zip Hooded Cardigan",
        "price_cad": 14.99,
        "original_price_cad": 29.99,
        "discount_pct": 50.0,
        "savings_cad": 15.00,
        "badge": "🔥 超级神价 (Steal)",
        "stars": "⭐⭐⭐⭐⭐",
        "value_tier": "ultra_high",
        "category": "clothes",
        "sizes": ["0-3M", "3-6M", "6-12M", "12-18M", "18-24M"],
        "in_stock": True,
        "product_url": "https://oldnavy.gapcanada.ca/browse/category.do?cid=60050",
        "image_url": "https://oldnavy.gapcanada.ca/Asset_Archive/ONWeb/assets/common/on-logo.png",
        "source": "Old Navy 50% Off Black Friday",
        "collection": "Old Navy Baby Deals"
    },
    # Gap Canada
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
    # Zara Canada
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
    # Carter's Canada
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
