# Deliberate cycle: the spellbook has not defined this function yet.
from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    normalized: str = "".join(
        char if char.isalpha() else " "
        for char in ingredients.lower()
    )
    words: list[str] = normalized.split()
    valid: bool = any(ingredient in words for ingredient in allowed)
    status: str = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
