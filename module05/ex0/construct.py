import sys
import os
import site


def main() -> None:
    venv_active: bool = sys.prefix != sys.base_prefix
    if venv_active:
        print("LABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.")

        print("\nReagent installation path:")
        print(site.getsitepackages()[0])
    else:
        print("LABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")

    print("\nGlobal package locations (outside virtual environment):")
    for path in site.getsitepackages([sys.base_prefix]):
        print(path)


if __name__ == "__main__":
    main()
