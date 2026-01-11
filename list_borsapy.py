import borsapy as bp

results = []
results.append("=" * 70)
results.append("BORSAPY TAM API REHBERİ")
results.append("=" * 70)

# 1. TICKER (Hisse Senedi)
results.append("\n1. TICKER (BIST Hisse Senetleri)")
results.append("-" * 50)
try:
    ticker = bp.Ticker("THYAO")
    methods = [x for x in dir(ticker) if not x.startswith('_')]
    results.append(f"Methods/Properties: {methods}")
except Exception as e:
    results.append(f"Error: {e}")

# 2. FUND (Yatırım Fonları)
results.append("\n2. FUND (TEFAS Fonları)")
results.append("-" * 50)
try:
    fund = bp.Fund("TCD")
    methods = [x for x in dir(fund) if not x.startswith('_')]
    results.append(f"Methods/Properties: {methods}")
except Exception as e:
    results.append(f"Error: {e}")

# 3. FX (Döviz ve Emtia)
results.append("\n3. FX (Döviz, Altın, Emtia)")
results.append("-" * 50)
try:
    fx = bp.FX("USD")
    methods = [x for x in dir(fx) if not x.startswith('_')]
    results.append(f"Methods/Properties: {methods}")
except Exception as e:
    results.append(f"Error: {e}")

# 4. CRYPTO
results.append("\n4. CRYPTO (Kripto)")
results.append("-" * 50)
try:
    crypto = bp.Crypto("BTCTRY")
    methods = [x for x in dir(crypto) if not x.startswith('_')]
    results.append(f"Methods/Properties: {methods}")
except Exception as e:
    results.append(f"Error: {e}")

# 5. INDEX (Endeksler)
results.append("\n5. INDEX (Endeksler)")
results.append("-" * 50)
try:
    idx = bp.Index("XU100")
    methods = [x for x in dir(idx) if not x.startswith('_')]
    results.append(f"Methods/Properties: {methods}")
except Exception as e:
    results.append(f"Error: {e}")

# 6. INFLATION
results.append("\n6. INFLATION (Enflasyon)")
results.append("-" * 50)
try:
    inf = bp.Inflation()
    methods = [x for x in dir(inf) if not x.startswith('_')]
    results.append(f"Methods/Properties: {methods}")
except Exception as e:
    results.append(f"Error: {e}")

# 7. SCREENER
results.append("\n7. SCREENER (Hisse Tarama)")
results.append("-" * 50)
try:
    screener = bp.Screener()
    methods = [x for x in dir(screener) if not x.startswith('_')]
    results.append(f"Methods/Properties: {methods}")
except Exception as e:
    results.append(f"Error: {e}")

# 8. Global Functions
results.append("\n8. GLOBAL FONKSİYONLAR")
results.append("-" * 50)
funcs = ['banks', 'bonds', 'companies', 'compare_funds', 'crypto_pairs', 
         'download', 'economic_calendar', 'index', 'indices', 
         'metal_institutions', 'risk_free_rate', 'screen_funds', 
         'screen_stocks', 'search_companies', 'search_funds', 
         'sectors', 'stock_indices']
for f in funcs:
    if hasattr(bp, f):
        results.append(f"bp.{f}()")

results.append("\n" + "=" * 70)

with open("borsa-mcp/borsapy_full_api.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("Check borsa-mcp/borsapy_full_api.txt")
