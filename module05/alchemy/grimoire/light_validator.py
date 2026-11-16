def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    normalized: str = "".join(
        wd if wd.isalpha() else " "
        for wd in ingredients.lower()
    )
    words: list[str] = normalized.split()
    allowed: list[str] = light_spell_allowed_ingredients()
    valid: bool = any(ingredient in words for ingredient in allowed)
    if valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
