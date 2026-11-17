# genpark-url-to-ad

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![MCP Dependency](https://img.shields.io/badge/MCP-mcp%20SDK-blue)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark URL-To-Ad is an autonomous advertising copy and performance prediction engine implementing OpenGraph semantic parsing, multi-angle conversion framework generation (PAS, BAB, Social Proof, FOMO, Feature-Benefit), and Bayesian Beta-Binomial conjugate CTR estimation.

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

## MCP Runtime Requirements

Use Python 3.10+ for the MCP server. The core `client.py` has no external dependencies; MCP transport requires `mcp>=1.0.0,<2`. From this checkout, install it into the Python environment used by your MCP client:

```bash
python -m pip install -r requirements.txt
```

Use the same Python interpreter to launch `mcp_server.py`. In desktop client configuration, set `command` to that interpreter's absolute path.

## Quickstart

```python
from client import GenParkUrlToAd

engine = GenParkUrlToAd()
res = engine.predict_bayesian_ctr_score(historical_impressions=10000, historical_clicks=250, ad_relevance_score=0.9)
print(res["calibrated_predicted_ctr_pct"], "% CTR")
```

## Local MCP Server

After installing the MCP requirements, launch the local STDIO server:

```bash
python mcp_server.py
```

Point your MCP client at the absolute path to `mcp_server.py` using the same Python interpreter. This repository does not provide a hosted MCP endpoint.

## License
MIT
