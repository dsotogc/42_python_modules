#!/usr/bin/env python3

import sys
from typing import IO


def main() -> None:
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
    else:
        file: IO[str] | None = None
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{sys.argv[1]}'")
            file = open(sys.argv[1])
            content: str = file.read()
            print(f"---\n\n{content}\n\n---")
        except IOError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            if file:
                file.close()
                print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
