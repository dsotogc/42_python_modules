from dotenv import load_dotenv
import os


def dbinfo(url: str | None) -> str:
    if not url:
        return "Database URL is missing"
    scheme, separator, address = url.partition("://")
    if not scheme or not separator:
        return "Invalid URL"
    host = address.split('/', 1)[0].rsplit('@', 1)[-1]
    if not host:
        return "Invalid URL"
    host = host.split(':', 1)[0].lower()
    if host in ("127.0.0.1", "localhost"):
        return "Local instance configured"
    return "External instance configured"


def checknetwork(url: str | None) -> str:
    if not url:
        return "Not given"
    if url.startswith("https://") or url.startswith("http://"):
        if url.split("://", 1)[1].split('/', 1)[0]:
            return "Endpoint configured (connection not tested)"
        return "Not valid"
    else:
        return "Not valid"


def display_info(config: dict[str, str | None]) -> None:
    print(f"Mode: {config['matrix_mode']}")
    print(f"Database: {dbinfo(config['database_url'])}")
    print(f"API Key: {'Configured' if config['api_key'] else 'Missing'}")
    print(f"Log Level: {config['log_level']}")
    print(f"Remote Network: {checknetwork(config['zion_endpoint'])}")
    if config['matrix_mode'] == "development":
        configured: int = sum(bool(value) for value in config.values())
        print(f"Development diagnostics: {configured}/{len(config)} "
              "configuration values present")
    else:
        print("Production: development diagnostics disabled")


def main() -> None:
    load_dotenv()
    mode: str = os.getenv("MATRIX_MODE", "development")
    if mode not in ("development", "production"):
        print("WARNING: Invalid MATRIX_MODE; using development.")
        mode = "development"
    config: dict[str, str | None] = {
        "matrix_mode": mode,
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "DEBUG" if mode == "development"
                               else "INFO"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT")
    }

    print("\nORACLE STATUS: Consulting the configuration...\n")

    print("Configuration (environment and .env, with defaults):")
    display_info(config)
    print("\nConfiguration check:")
    for name, value in config.items():
        if not value:
            print(f"[WARNING] Missing {name.upper()}")
    if all(config.values()):
        print("[OK] All configuration values are present")


if __name__ == "__main__":
    main()
