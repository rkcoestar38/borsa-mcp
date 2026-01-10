
import borsapy as bp
import json
import sys

# Force UTF-8 for stdout
sys.stdout.reconfigure(encoding='utf-8')

def safe_serialize(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    if isinstance(obj, dict):
        return {k: safe_serialize(v) for k, v in obj.items()}
    if hasattr(obj, '__dict__'):
        return {k: safe_serialize(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
    return str(obj)

print("DATA_START")

# THYAO
print("SECTION: THYAO")
try:
    ticker = bp.Ticker("THYAO")
    # info usually returns the data dict or object
    data = ticker.info
    print(json.dumps(safe_serialize(data), indent=2, ensure_ascii=False))
except Exception as e:
    print(f"ERROR: {e}")

# TTE
print("SECTION: TTE")
try:
    fund = bp.Fund("TTE")
    # trying to get profile/info
    # borsapy Fund often has .profile or .info
    if hasattr(fund, 'profile'):
        print(json.dumps(safe_serialize(fund.profile), indent=2, ensure_ascii=False))
    elif hasattr(fund, 'info'):
        print(json.dumps(safe_serialize(fund.info), indent=2, ensure_ascii=False))
    else:
        print(f"FUND_RAW: {fund}")
except Exception as e:
    print(f"ERROR: {e}")

# INFLATION
print("SECTION: INFLATION")
try:
    inflation = bp.Inflation()
    # Looking for calculation
    # Only if calculate exists
    if hasattr(inflation, 'calculate'):
        res = inflation.calculate(10000, 2021) # defaulting end year
        print(json.dumps(safe_serialize(res), indent=2, ensure_ascii=False))
    else:
        print("INFLATION_NOT_SUPPORTED_OR_METHOD_UNKNOWN")
        # Try to print dir to see options if needed
        # print(dir(inflation))
except Exception as e:
    print(f"ERROR: {e}")

print("DATA_END")
