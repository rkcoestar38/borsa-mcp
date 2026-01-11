import borsapy as bp
from borsapy import fx as fx_module
import inspect

# Get full source of FX module
source = inspect.getsource(fx_module)

# Write first 5000 chars
with open("borsa-mcp/fx_full_source.txt", "w", encoding="utf-8") as f:
    f.write(source[:8000])

print("Written first 8000 chars to borsa-mcp/fx_full_source.txt")
