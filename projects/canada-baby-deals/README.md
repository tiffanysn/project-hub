# 🍁 Canada Baby Girl Deals Crawler (加拿大女宝宝黑五 & 12月大促折扣汇集器)

专为加拿大有女宝宝（0~24M / 幼童）的家庭打造的折扣监控与性价比汇总爬虫。

重点覆盖 **衣服/雪服、鞋子/雪靴、益智玩具、家居/睡袋/包被**，特别精选 **12 大加拿大高性价比与口碑母婴品牌**：
- **The Children's Place (TCP)**：加拿大平价之王，$4.99~$9.99 门票爆款、摇粒绒睡衣与红格纹节日裙
- **优衣库 (Uniqlo Canada)**：冬季神级打底，婴儿 Heattech 发热包屁衣、摇粒绒连体衣、轻暖空气棉服
- **Nest Designs (温哥华母婴)**：温哥华本土高端竹纤维/有机棉，0.5/1.0/2.5 TOG 恒温睡袋、分腿睡袋与软糯爬服
- **Deux par Deux (DPD)**：魁北克著名设计师童装与高端防寒雪服，清仓直降 5 折
- **Stonz**：温哥华顶级婴儿保暖雪靴 (Booties)、防水手套、学步软底鞋
- **Loulou Lollipop (温哥华母婴)**：高颜值 Tencel 莫代尔睡衣、秋冬 2.5 TOG 睡袋、食品级硅胶牙胶玩具
- **Konny**：超人气人体工学背带、360度旋转围兜、秋冬加厚打底与保暖睡袋
- **H&M Canada**：会员黑五特惠，有机棉多件装长袖包屁衣、荷叶边针织裙、羊羔绒保暖连体衣
- **Carter's (OshKosh / Child of Mine)**：加拿大全境高性价比门票爆款 (Doorbusters)、纯棉爬服多件装
- **Gap Canada & Old Navy**：黑五全场 5 折起，有机棉连体衣与小熊耳朵加绒外套
- **Zara Canada**：黑五及 Boxing Day 节日季特惠，复古粉针织裙与软底学步鞋
- **Joe Fresh (加拿大国民品牌)**：Superstore 旗下平价优选，轻薄保暖羽绒雪服与抓绒爬服

---

## 🌟 核心功能

1. **多源双引擎数据采集**：
   - **Shopify 官方实时引擎**：直连 Stonz、Deux par Deux、Konny 官方实时商品库，精准抓取现价、原价、现存尺码及商品高清图。
   - **Flipp 加拿大全境海报与零售引擎**：抓取 Walmart CA、Carter's、Toys R Us 等全境各大实体与线上零售商黑五及节日特惠。
   - **精选大促策略库**：Gap、Zara、H&M 黑五前夕开抢时间表、省钱攻略与专场直达。
2. **女宝宝属性智能过滤**：
   - 自动过滤纯男童款式，优先聚合女童款及柔和中性款（粉调、碎花、连衣裙、蕾丝、雪靴、包被）。
3. **高性价比 (Cost-Performance) 打分系统**：
   - 自动计算折扣率：`🔥 5折+ 超级神价`、`🏷️ 高性价比 (30%~49%)`、`💰 $20加币以下白菜价`。
4. **多形态数据输出**：
   - **交互式 Web 可视化看板**：[`data/deals_dashboard.html`](./data/deals_dashboard.html)（带商品缩略图、尺码、现价/原价、直达购买链接与品类筛选）。
   - **CSV 数据表**：[`data/deals.csv`](./data/deals.csv)
   - **JSON 数据源**：[`data/deals.json`](./data/deals.json)

---

## 🚀 快速启动

本项目采用零外部依赖设计（内置使用 Python 标准库），任何 Mac 环境下均可直接运行：

### 1. 一键抓取全部好价并生成看板
```bash
python3 main.py
```

### 2. 命令行进阶选项
```bash
# 只抓取 Stonz 婴儿雪靴与手套
python3 main.py --brand stonz

# 只看鞋靴类折扣
python3 main.py --category shoes

# 筛选 40% OFF 以上的高性价比好物
python3 main.py --min-discount 40

# 指定加拿大邮编（针对零售商实体店海报）
python3 main.py --postal-code V6B2W9  # 温哥华邮编
```

### 3. 查看交互式可视化看板
抓取完成后，在终端运行以下命令，即可在浏览器中打开精美的折扣看板：
```bash
open data/deals_dashboard.html
```
