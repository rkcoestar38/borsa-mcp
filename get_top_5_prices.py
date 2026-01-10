
import sys
import os
import json

# Add the directory to sys.path
sys.path.append(r"C:\Users\ridva\Documents\antigravity\budget-app\borsa-mcp")

from mcp_server import get_stock_price

symbols = ["ASELS", "KILER", "GARAN", "ENKAI", "THYAO", "TUPRS", "KCHOL"]
results = {}

for symbol in symbols:
    try:
        raw_res = get_stock_price(symbol)
        results[symbol] = json.loads(raw_res)
    except Exception as e:
        results[symbol] = {"error": str(e)}

print(json.dumps(results, indent=2, ensure_ascii=False))
