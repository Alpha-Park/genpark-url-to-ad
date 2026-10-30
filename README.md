# genpark-url-to-ad

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark URL-To-Ad is a zero-dependency autonomous advertising copy and performance prediction engine implementing OpenGraph semantic parsing, multi-angle conversion framework generation (PAS, BAB, Social Proof, FOMO, Feature-Benefit), and Bayesian Beta-Binomial conjugate CTR estimation.

```mermaid
flowchart TD
    A[Webpage Metadata & Microdata] --> B[Semantic Signal Extractor]
    B --> C[5 Conversion Copy Angle Composer]
    C --> D[Flesch-Kincaid Readability Auditor]
    E[Historical Impression & Click Data] --> F[Conjugate Beta Prior Model]
    F --> G[Bayesian CTR Posterior & 95% CI]
    G --> H[Budget Scale & Copy Optimization Action]
```

## Features
- **Semantic Metadata Signal Scorer**: Parses OpenGraph and schema attributes into structured product entities with readiness validation.
- **5-Angle Conversion Copywriting**: Formulates PAS, BAB, Authority, Scarcity, and Benefit angles with readability metrics.
- **Conjugate Bayesian CTR Estimator**: Computes calibrated click-through rate posteriors and 95% credible intervals with Beta distributions.

## Quickstart

```python
from client import GenParkUrlToAd

engine = GenParkUrlToAd()
res = engine.predict_bayesian_ctr_score(historical_impressions=10000, historical_clicks=250, ad_relevance_score=0.9)
print(res["calibrated_predicted_ctr_pct"], "% CTR")
```

## License
MIT
