# -*- coding: utf-8 -*-
"""
GenPark URL-To-Ad Client
Zero-dependency semantic OpenGraph/metadata signal parser, 5-angle conversion ad hook composer,
and conjugate Beta-Binomial Bayesian CTR prediction engine.
"""

import math
from typing import Dict, List, Any, Optional

class GenParkUrlToAd:
    """
    Parses product webpage metadata, composes persuasive conversion copy angles,
    and calculates posterior Bayesian CTR expectations.
    """

    def extract_semantic_ad_signals(
        self,
        html_or_meta: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Extracts OpenGraph, Twitter Card, and Product Schema signals and scores semantic readiness.
        """
        title = html_or_meta.get("og:title") or html_or_meta.get("title") or "Unnamed Product"
        desc = html_or_meta.get("og:description") or html_or_meta.get("description") or ""
        image = html_or_meta.get("og:image") or html_or_meta.get("image") or ""
        price = html_or_meta.get("price") or html_or_meta.get("product:price:amount")
        currency = html_or_meta.get("currency") or html_or_meta.get("product:price:currency") or "USD"
        rating = html_or_meta.get("rating") or html_or_meta.get("aggregateRating:ratingValue")

        # Completeness scoring
        completeness = 0
        if title: completeness += 30
        if desc and len(desc) > 20: completeness += 30
        if image: completeness += 20
        if price: completeness += 10
        if rating: completeness += 10

        # Extract value keywords
        words = [w.strip(" .,!?:;()[]{}") for w in desc.lower().split()]
        buzzwords = ["ai", "fast", "easy", "pro", "save", "boost", "ultimate", "smart", "automated", "zero"]
        detected_hooks = [w for w in set(words) if w in buzzwords]

        return {
            "title": title,
            "description": desc,
            "image_url": image,
            "price": float(price) if price is not None else None,
            "currency": currency,
            "rating": float(rating) if rating is not None else None,
            "semantic_completeness_score": completeness,
            "is_ad_ready": completeness >= 70,
            "detected_value_hooks": detected_hooks
        }

    def compose_multi_angle_ad_hooks(
        self,
        product_name: str,
        category: str,
        key_benefits: List[str],
        target_audience: str,
        discount_offer: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Composes 5 high-converting advertising copy angles with Flesch-Kincaid readability scoring.
        """
        b1 = key_benefits[0] if key_benefits else "boost productivity"
        b2 = key_benefits[1] if len(key_benefits) > 1 else "automate repetitive tasks"
        offer_str = f" Claim {discount_offer} today!" if discount_offer else " Try it risk-free today!"

        angles = {
            "pas_problem_agitate_solve": {
                "headline": f"Tired of struggling with {category.lower()}?",
                "body": f"Manual workflows waste hours every week. {product_name} eliminates friction with {b1} and {b2}.{offer_str}",
                "cta": "Get Started Now"
            },
            "bab_before_after_bridge": {
                "headline": f"Imagine effortless {category.lower()}.",
                "body": f"Yesterday you spent hours configuring setups. Tomorrow with {product_name}, you unlock {b1} in seconds.{offer_str}",
                "cta": "See How It Works"
            },
            "social_proof_authority": {
                "headline": f"Why top {target_audience} choose {product_name}.",
                "body": f"Thousands of teams rely on {product_name} for {b1}. Rated 4.9/5 by industry leaders.{offer_str}",
                "cta": "Join the Top 1%"
            },
            "fomo_scarcity": {
                "headline": f"Don't fall behind in {category}.",
                "body": f"Your competitors are already scaling with {b1}. Don't miss out on {product_name}.{offer_str}",
                "cta": "Claim Your Access"
            },
            "feature_benefit": {
                "headline": f"Engineered for {target_audience}.",
                "body": f"{product_name} delivers instant {b1} and seamless {b2} with zero learning curve.{offer_str}",
                "cta": "Start Free Trial"
            }
        }

        # Calculate average word count and reading ease for each angle
        for angle_name, data in angles.items():
            full_text = f"{data['headline']} {data['body']} {data['cta']}"
            words = full_text.split()
            word_count = len(words)
            char_count = sum(len(w) for w in words)
            # Flesch-Kincaid Reading Ease heuristic
            avg_word_len = char_count / max(1, word_count)
            ease_score = max(0.0, min(100.0, 206.835 - (1.015 * word_count) - (84.6 * (avg_word_len / 5.0))))
            data["word_count"] = word_count
            data["reading_ease_score"] = round(ease_score, 1)

        return {
            "product_name": product_name,
            "category": category,
            "target_audience": target_audience,
            "angles_generated": len(angles),
            "angles": angles
        }

    def predict_bayesian_ctr_score(
        self,
        historical_impressions: int,
        historical_clicks: int,
        ad_relevance_score: float,
        prior_ctr_alpha: float = 2.0,
        prior_ctr_beta: float = 98.0
    ) -> Dict[str, Any]:
        """
        Predicts Expected CTR using conjugate Beta-Binomial Bayesian updating.
        Posterior Mean = (alpha + clicks) / (alpha + beta + impressions)
        """
        if historical_impressions < 0 or historical_clicks < 0:
            raise ValueError("Impressions and clicks must be non-negative.")
        if historical_clicks > historical_impressions:
            raise ValueError("Clicks cannot exceed impressions.")

        # Beta posterior parameters
        alpha_post = prior_ctr_alpha + historical_clicks
        beta_post = prior_ctr_beta + (historical_impressions - historical_clicks)

        posterior_mean_ctr = alpha_post / (alpha_post + beta_post)
        
        # Posterior variance: (alpha * beta) / ((alpha + beta)^2 * (alpha + beta + 1))
        total_n = alpha_post + beta_post
        posterior_var = (alpha_post * beta_post) / (total_n * total_n * (total_n + 1))
        posterior_std = math.sqrt(posterior_var)

        # 95% Credible Interval (normal approximation)
        ci_lower = max(0.0, posterior_mean_ctr - 1.96 * posterior_std)
        ci_upper = min(1.0, posterior_mean_ctr + 1.96 * posterior_std)

        # Calibrated CTR incorporating ad relevance (relevance 0-1 adjusts posterior mean by up to +/- 20%)
        relevance_factor = 0.8 + 0.4 * max(0.0, min(1.0, ad_relevance_score))
        calibrated_ctr = round(posterior_mean_ctr * relevance_factor, 5)

        return {
            "historical_impressions": historical_impressions,
            "historical_clicks": historical_clicks,
            "ad_relevance_score": ad_relevance_score,
            "prior_expected_ctr_pct": round(100.0 * (prior_ctr_alpha / (prior_ctr_alpha + prior_ctr_beta)), 2),
            "posterior_expected_ctr_pct": round(100.0 * posterior_mean_ctr, 3),
            "calibrated_predicted_ctr_pct": round(100.0 * calibrated_ctr, 3),
            "credible_interval_95_pct": [round(100.0 * ci_lower, 3), round(100.0 * ci_upper, 3)],
            "posterior_uncertainty_std_pct": round(100.0 * posterior_std, 4),
            "recommendation": "SCALE_BUDGET" if calibrated_ctr >= 0.035 else ("OPTIMIZE_COPY" if calibrated_ctr >= 0.015 else "RETEST_ANGLE")
        }
