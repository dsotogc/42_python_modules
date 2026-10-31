#!/usr/bin/env python3

import sys
from typing import IO


def main() -> None:
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
    else:
        file: IO[str] | None = None
        success: bool = False
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{sys.argv[1]}'")
            file = open(sys.argv[1])
            content: str = file.read()
            new_content: str = content.replace('\n', "#\n") + "#"
            print(f"---\n\n{content}\n\n---")
            success = True
        except IOError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            if file:
                file.close()
                print(f"File '{sys.argv[1]}' closed.")

        if success:
            print("\nTransform data:")
            print(f"---\n\n{new_content}\n\n---")
            nfile_name: str = input("Enter new dile name (or empty): ")
            if nfile_name:
                new_file: IO[str] | None = None
                try:
                    new_file = open(nfile_name, "w")
                    print(f"Saving data to '{nfile_name}'")
                    new_file.write(new_content)
                except IOError as e:
                    print(f"Error creating file '{nfile_name}': {e}")
                finally:
                    if new_file:
                        new_file.close()
                        print(f"Data saved in file '{nfile_name}'")


if __name__ == "__main__":
    main()
