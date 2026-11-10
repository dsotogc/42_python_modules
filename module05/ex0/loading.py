import importlib

REAGENTS: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
}


def check_reagent(name: str, purpose: str) -> bool:
    try:
        module = importlib.import_module(name)
    except ImportError:
        print(f"[MISSING] {name} - {purpose} unavailable")
        print(f"  pip:    pip install {name}")
        print(f"  Poetry: poetry add {name}")
        return False
    version: str = str(getattr(module, "__version__", "unknown"))
    print(f"[OK] {name} ({version}) - {purpose} ready")
    return True


def explain_tools() -> None:
    print("pip vs Poetry:")
    print("  requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    results: list[bool] = [
        check_reagent(name, purpose) for name, purpose in REAGENTS.items()
    ]
    print()
    explain_tools()
    print()
    if all(results):
        print("All reagents present and accounted for.")
    else:
        print("Some reagents are missing. "
              "Install them with the commands above.")


if __name__ == "__main__":
    main()