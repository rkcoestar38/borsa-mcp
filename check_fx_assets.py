import borsapy as bp
import traceback

with open("borsa-mcp/fx_assets_list.txt", "w", encoding="utf-8") as f:
    f.write("SUPPORTED FX ASSETS:\n")
    f.write("="*70 + "\n\n")
    
    try:
        fx = bp.FX("INVALID_ASSET_12345")
    except bp.DataNotAvailableError as e:
        f.write(f"DataNotAvailableError: {e}\n\n")
    except Exception as e:
        f.write(f"Exception Type: {type(e).__name__}\n")
        f.write(f"Message: {e}\n")
        f.write(f"Full traceback:\n{traceback.format_exc()}\n")
    
    f.write("\n" + "="*70 + "\n")
    
    # Also try to find any constants in the module
    f.write("\nModule contents with 'asset' or 'fx':\n")
    for name in dir(bp):
        if 'asset' in name.lower() or 'fx' in name.lower():
            f.write(f"  {name}\n")
    
    f.write("\nDONE")

print("Check borsa-mcp/fx_assets_list.txt")
