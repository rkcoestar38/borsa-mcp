
import borsapy as bp
import json
from datetime import datetime

def _serialize(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    if hasattr(obj, '__dict__'):
        return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}
    return str(obj)

print("--- TOOL: get_stock_price('THYAO') ---")
try:
    ticker = bp.Ticker("THYAO")
    # Ticker info might be a property or method depending on version, 
    # relying on my previous code assumption that `.info` exists.
    # If not, printing dir(ticker) to debug.
    if hasattr(ticker, 'info'):
        print(json.dumps(ticker.info, indent=2, default=str, ensure_ascii=False))
    else:
        # Fallback if structure is different
        print(f"Ticker object: {ticker}")
        try:
            print(json.dumps(ticker.get_summary(), indent=2, default=str, ensure_ascii=False))
        except:
            pass
except Exception as e:
    print(f"Error: {e}")

print("\n--- TOOL: get_fund_info('TTE') ---")
try:
    fund = bp.Fund("TTE")
    if hasattr(fund, 'info'):
        print(json.dumps(fund.info, indent=2, default=str, ensure_ascii=False))
    else:
        print(f"Fund object: {fund}")
except Exception as e:
    print(f"Error: {e}")

print("\n--- TOOL: calculate_inflation(10000, 2021) ---")
try:
    inflation = bp.Inflation()
    # Assuming calculate method exists or similar
    # If not, we print available methods/properties
    try:
        # Common pattern: calculate(amount, start_year, end_year)
        # Checking if 'calculate' exists
        if hasattr(inflation, 'calculate'):
            res = inflation.calculate(10000, 2021, datetime.now().year)
            print(json.dumps(res, indent=2, default=str, ensure_ascii=False))
        else:
            print("Inflation object created, but 'calculate' method not found. Available attributes:")
            print(dir(inflation))
    except Exception as e:
        print(f"Error in calculation: {e}")
except Exception as e:
    print(f"Error: {e}")
