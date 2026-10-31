#!/usr/bin/env python3

def secure_archive(
        fname: str,
        action: str = "read",
        content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "write":
            with open(fname, "w", encoding="utf-8") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(fname, "r", encoding="utf-8") as f:
                data: str = f.read()
            return (True, data)
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    output: tuple[bool, str] = secure_archive("hola.txt")
    print(output)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "write", output[1]))


if __name__ == "__main__":
    main()
