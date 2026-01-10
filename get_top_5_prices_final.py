
import borsapy as bp
import json
import re

symbols = ["ASELS", "KILER", "GARAN", "ENKAI", "THYAO", "TUPRS", "KCHOL"]
results = {}

for symbol in symbols:
    try:
        ticker = bp.Ticker(symbol)
        info = str(ticker.info if hasattr(ticker, 'info') else ticker)
        
        # Regex to find last price in the EnrichedInfo string
        match = re.search(r"'last':\s*([\d\.]+)", info)
        if match:
            results[symbol] = float(match.group(1))
        else:
            results[symbol] = "Price not found"
    except Exception as e:
        results[symbol] = f"Error: {e}"

print(json.dumps(results, indent=2, ensure_ascii=False))
