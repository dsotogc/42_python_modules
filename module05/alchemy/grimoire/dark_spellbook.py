from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation: str = dark_validate_ingredients(ingredients)
    decision: str = (
        "recorded" if validation.endswith(" - VALID") else "rejected"
    )
    return f"Spell {decision}: {spell_name} ({validation})"
