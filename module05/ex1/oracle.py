from dotenv import load_dotenv
import os


def dbinfo(url: str | None) -> str:
    if not url:
        return "Database URL is missing"
    else:
        try:
            host = url.rsplit('@', 1)[1].split('/', 1)[0].split(':', 1)[0]
        except IndexError:
            return "Invalid URL"
        if host == "127.0.0.1" or host == "localhost":
            return "Connected to local instance"
        return "Connected to external instance"


def checknetwork(url: str | None) -> str:
    if not url:
        return "Not given"
    if url.startswith("https://") or url.startswith("http://"):
        return "Online"
    else:
        return "Not valid"


def display_info(config: dict[str, str | None]) -> None:
    print(f"Mode: {config['matrix_mode']}")
    print(f"Database: {dbinfo(config['database_url'])}")
    print(f"API Access: {'Authenticated' if config['api_key'] else 'Failed'}")
    print(f"Log Level: {config['log_level']}")
    print(f"Remote Network: {config['z_endpoint']}")


def main() -> None:
    env_loaded: bool = load_dotenv()
    config: dict[str, str] = {
        "matrix_mode": os.getenv("MATRIX_MODE", "development"),
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "DEBUG"),
        "z_endpoint": os.getenv("ZION_ENDPOINT")
    }

    print("\nORACLE STATUS: Consulting the configuration...\n")

    if env_loaded:
        print("Configuration loaded:")
        display_info(config)
    else:
        print("Configuration is missing, showing default values:")
        display_info(config)


if __name__ == "__main__":
    main()
