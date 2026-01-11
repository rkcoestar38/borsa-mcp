import requests

BASE = "http://localhost:8000"
tests = [
    ("GET", "/api/market/fx/USD"),
    ("GET", "/api/market/gold/all"),
    ("GET", "/api/market/stock/info/THYAO"),
    ("GET", "/api/market/fund/detail/TCD"),
    ("GET", "/api/market/crypto/BTCTRY"),
    ("GET", "/api/market/index/XU100"),
    ("GET", "/api/market/risk-free-rate"),
    ("GET", "/api/market/bond/rates"),
    ("GET", "/api/market/stock/news/THYAO"),
    ("GET", "/api/market/stock/financials/THYAO"),
    ("GET", "/api/market/viop/futures"),
]

print("Testing key endpoints...")
passed = 0
failed = 0

for method, ep in tests:
    try:
        r = requests.get(BASE + ep, timeout=30)
        d = r.json()
        if d.get("success"):
            print(f"[OK] {ep}")
            passed += 1
        else:
            err = str(d.get("error", "unknown"))[:60]
            print(f"[WARN] {ep}")
            print(f"       Error: {err}")
            failed += 1
    except Exception as e:
        print(f"[FAIL] {ep}")
        print(f"       Exception: {str(e)[:60]}")
        failed += 1

print(f"\nResults: {passed} passed, {failed} failed")
