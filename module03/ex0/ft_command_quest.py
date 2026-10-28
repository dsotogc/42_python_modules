#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    argc: int = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    if argc == 1:
        print("No arguments provided!")
    else:
        i: int = 1
        print(f"Arguments received: {argc - 1}")
        while i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
