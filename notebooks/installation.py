import sys


async def install():
    if "micropip" in sys.modules:
        import micropip

        await micropip.install(["numpy", "pandas", "altair", "matplotlib"])
        await micropip.install(
            "https://raw.githubusercontent.com/LedgerInvesting/bermuda-clrs-workshop-2025/jupyterlite-setup/wheels/bermuda_ledger-2.1.15-py3-none-any.whl"
        )
    else:
        try:
            import bermuda
        except:
            print("Run: !pip install bermuda-ledger")
