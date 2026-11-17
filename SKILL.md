---
name: genpark-url-to-ad
description: Automated e-commerce short video factory.
---
# genpark-url-to-ad

An open-source GenPark alternative to Glato AI.

Paste any product URL. The agent scrapes the copy, rewrites a viral short-form script, generates voiceover via local TTS, and stitches together an ad video using FFmpeg.

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.
