# -*- coding: utf-8 -*-
"""
GenPark URL-To-Ad FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkUrlToAd

mcp = FastMCP("genpark-url-to-ad")
ad_engine = GenParkUrlToAd()

@mcp.tool()
def extract_semantic_ad_signals(html_or_meta_json: str) -> str:
    """
    Extracts OpenGraph, Twitter Card, and Product Schema signals and scores semantic readiness.
    """
    data = json.loads(html_or_meta_json)
    res = ad_engine.extract_semantic_ad_signals(data)
    return json.dumps(res, indent=2)

@mcp.tool()
def compose_multi_angle_ad_hooks(
    product_name: str,
    category: str,
    key_benefits_json: str,
    target_audience: str,
    discount_offer: Optional[str] = None
) -> str:
    """
    Composes 5 high-converting advertising copy angles with Flesch-Kincaid readability scoring.
    """
    benefits = json.loads(key_benefits_json)
    res = ad_engine.compose_multi_angle_ad_hooks(product_name, category, benefits, target_audience, discount_offer)
    return json.dumps(res, indent=2)

@mcp.tool()
def predict_bayesian_ctr_score(
    historical_impressions: int,
    historical_clicks: int,
    ad_relevance_score: float,
    prior_ctr_alpha: float = 2.0,
    prior_ctr_beta: float = 98.0
) -> str:
    """
    Predicts Expected CTR using conjugate Beta-Binomial Bayesian updating.
    """
    res = ad_engine.predict_bayesian_ctr_score(historical_impressions, historical_clicks, ad_relevance_score, prior_ctr_alpha, prior_ctr_beta)
    return json.dumps(res, indent=2)

def main():
    print("Testing URL to Ad:")
    print(predict_bayesian_ctr_score(5000, 120, 0.9))

if __name__ == "__main__":
    main()
