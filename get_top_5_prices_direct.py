
import borsapy as bp
import json

symbols = ["ASELS", "KILER", "GARAN", "ENKAI", "THYAO", "TUPRS", "KCHOL"]
results = {}

for symbol in symbols:
    try:
        ticker = bp.Ticker(symbol)
        # Handle different borsapy versions/returns
        if hasattr(ticker, 'info'):
            data = ticker.info
        else:
            data = ticker
            
        # Simplified for user output
        if hasattr(data, 'last'):
            price = data.last
        elif hasattr(data, 'to_dict'):
            price = data.to_dict().get('last', 'N/A')
        elif isinstance(data, dict):
            price = data.get('last', 'N/A')
        else:
            price = str(data)
            
        results[symbol] = price
    except Exception as e:
        results[symbol] = f"Error: {e}"

print(json.dumps(results, indent=2, ensure_ascii=False))
