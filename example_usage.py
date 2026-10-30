# -*- coding: utf-8 -*-
import json
from client import GenParkUrlToAd

engine = GenParkUrlToAd()

# 1. Semantic Metadata Extraction
page_data = {
    "og:title": "AlphaPark UltraFlow - Autonomous ETL Agent",
    "og:description": "Automate data pipelines with AI agents. Fast, resilient, and zero-code setup.",
    "og:image": "https://alphapark.io/assets/flow.png",
    "price": 49.0,
    "currency": "USD",
    "rating": 4.9
}
signals = engine.extract_semantic_ad_signals(page_data)
print(f"Extracted Signals: '{signals['title']}' | Score: {signals['semantic_completeness_score']}/100 | Ready={signals['is_ad_ready']}")

# 2. Multi-Angle Conversion Copy Hooks
hooks = engine.compose_multi_angle_ad_hooks(
    product_name="UltraFlow",
    category="Data Engineering Tools",
    key_benefits=["reduce data pipeline latency by 80%", "eliminate pipeline maintenance downtime"],
    target_audience="Data Engineers & CTOs",
    discount_offer="30% OFF Early Bird"
)
print()
print("Generated Copy Angles:")
for angle, content in hooks["angles"].items():
    print(f"  [{angle.upper()}] Readability: {content['reading_ease_score']}")
    print(f"    Headline: {content['headline']}")
    print(f"    Body: {content['body']}")

# 3. Bayesian CTR Estimation
ctr = engine.predict_bayesian_ctr_score(
    historical_impressions=12500,
    historical_clicks=380,
    ad_relevance_score=0.92
)
print()
print(f"Bayesian CTR: Calibrated={ctr['calibrated_predicted_ctr_pct']}% (95% CI: {ctr['credible_interval_95_pct'][0]}% - {ctr['credible_interval_95_pct'][1]}%) | Action: {ctr['recommendation']}")
