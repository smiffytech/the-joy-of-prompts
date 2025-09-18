#!/usr/bin/env python3

import json, sys, re
from pathlib import Path

# 1) Pick tokenizer like TickToken
try:
    import tiktoken
    try:
        enc = tiktoken.get_encoding("o200k_base")
    except Exception:
        enc = tiktoken.get_encoding("cl100k_base")  # fallback
except ImportError:
    print("Please: pip install tiktoken")
    sys.exit(1)

# 2) Inputs
if len(sys.argv) < 2:
    print("Usage: python count_tokens.py /path/to/conversations.json [title_filter]")
    sys.exit(1)

json_path = Path(sys.argv[1])
title_filter = sys.argv[2].lower() if len(sys.argv) > 2 else None

# 3) Load conversations
data = json.loads(json_path.read_text(encoding="utf-8"))

# 4) Accumulators
prompt_tokens = 0   # system + user (your questions/instructions)
response_tokens = 0 # assistant replies

def count(s: str) -> int:
    return len(enc.encode(s or ""))

# 5) Walk matching conversations
for convo in data:
    title = (convo.get("title") or "").lower()
    if title_filter and title_filter not in title:
        continue
    for msg in convo.get("mapping", {}).values():
        m = msg.get("message")
        if not m: 
            continue
        role = m.get("author", {}).get("role")
        parts = m.get("content", {}).get("parts") or []
        text = "\n".join(p for p in parts if isinstance(p, str))
        if role in ("system", "user", "tool"):  # count all non-assistant as "prompt" side
            prompt_tokens += count(text)
        elif role == "assistant":
            response_tokens += count(text)

# 6) Report token counts
print(f"Prompt tokens (user/system/tool): {prompt_tokens}")
print(f"Response tokens (assistant):       {response_tokens}")

# 7) Pricing (GPT-5 per public reports; unofficial)
USD_PER_M_IN = 1.25     # $ per 1M input tokens
USD_PER_M_OUT = 10.00   # $ per 1M output tokens

cost_usd = (prompt_tokens / 1_000_000) * USD_PER_M_IN + (response_tokens / 1_000_000) * USD_PER_M_OUT

# 8) FX: A$1 = $0.6651 USD  ->  $1 USD = A$1.503533...
USD_TO_AUD = 1 / 0.6651
cost_aud = cost_usd * USD_TO_AUD

print(f"Estimated cost:  USD ${cost_usd:,.4f}")
print(f"Estimated cost:  AUD A${cost_aud:,.4f}")
