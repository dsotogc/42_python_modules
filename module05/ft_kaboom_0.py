import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    recorded: str = alchemy.grimoire.light_spell_record(
        "Fantasy", "Earth, wind and fire"
    )
    print(f"Testing record light spell: {recorded}")
    rejected: str = alchemy.grimoire.light_spell_record(
        "Stonework", "stones and sand"
    )
    print(f"Testing rejected light spell: {rejected}")


if __name__ == "__main__":
    main()
