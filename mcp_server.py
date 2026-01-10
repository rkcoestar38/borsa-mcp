#!/usr/bin/env python3
"""
Borsa Data MCP Server - Instant startup version.
Uses minimal imports for fastest possible startup.
"""
import sys
import json

# CRITICAL: FastMCP import at the very end after tool definitions would be ideal,
# but we need it for decorators. However, we can delay other imports.

def _serialize(obj):
    """Convert any object to JSON-serializable format"""
    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj
    if isinstance(obj, list):
        return [_serialize(i) for i in obj]
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    if hasattr(obj, 'keys'):
        return {k: _serialize(obj[k]) for k in obj.keys()}
    if hasattr(obj, '__dict__'):
        return {k: _serialize(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
    return str(obj)

# Lazy loader for borsapy - only imports when actually needed
_bp_module = None
def _get_bp():
    global _bp_module
    if _bp_module is None:
        import borsapy
        _bp_module = borsapy
    return _bp_module

# Import FastMCP as late as possible in the import chain
from fastmcp import FastMCP
mcp = FastMCP("borsa-data")

@mcp.tool()
def ping() -> str:
    """Health check - returns server status immediately."""
    return '{"status":"ok","server":"borsa-data","version":"3.0"}'

@mcp.tool()
def get_stock_price(symbol: str) -> str:
    """
    Get the current stock price for a BIST symbol.
    Args:
        symbol: Stock ticker (e.g., THYAO, ASELS, GARAN, EREGL, TUPRS)
    """
    try:
        bp = _get_bp()
        ticker = bp.Ticker(symbol.upper())
        data = ticker.info if hasattr(ticker, 'info') else ticker
        return json.dumps(_serialize(data), indent=2, default=str, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e), "symbol": symbol}, ensure_ascii=False)

@mcp.tool()
def get_fund_info(fund_code: str) -> str:
    """
    Get detailed information about a TEFAS mutual fund.
    Args:
        fund_code: TEFAS fund code (e.g., TTE, AFA, TLY, AFT)
    """
    try:
        bp = _get_bp()
        fund = bp.Fund(fund_code.upper())
        data = fund.info if hasattr(fund, 'info') else (fund.profile if hasattr(fund, 'profile') else fund)
        return json.dumps(_serialize(data), indent=2, default=str, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e), "fund_code": fund_code}, ensure_ascii=False)

@mcp.tool()
def get_fx_rate(pair: str = "USDTRY") -> str:
    """
    Get the current exchange rate for a currency pair.
    Args:
        pair: Currency pair (e.g., USDTRY, EURTRY, GBPTRY)
    """
    try:
        bp = _get_bp()
        ticker = bp.Ticker(pair.upper())
        data = ticker.info if hasattr(ticker, 'info') else ticker
        return json.dumps(_serialize(data), indent=2, default=str, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e), "pair": pair}, ensure_ascii=False)

@mcp.tool()
def calculate_inflation(amount: float, from_year: int, to_year: int = None) -> str:
    """
    Calculate inflation-adjusted value using Turkish CPI data.
    Args:
        amount: Original amount in TRY
        from_year: Starting year (e.g., 2020)
        to_year: Target year (default: current year)
    """
    from datetime import datetime
    if to_year is None:
        to_year = datetime.now().year
    try:
        bp = _get_bp()
        inflation = bp.Inflation()
        if hasattr(inflation, 'calculate'):
            result = inflation.calculate(amount, from_year, to_year)
            return json.dumps(_serialize(result), indent=2, default=str, ensure_ascii=False)
        return json.dumps({"error": "Inflation API not available"})
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)

if __name__ == "__main__":
    mcp.run()
