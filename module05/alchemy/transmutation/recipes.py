from alchemy.elements import create_air
from elements import create_fire
from ..potions import strength_potion


def lead_to_gold() -> str:
    c_air: str = create_air()
    c_sp: str = strength_potion()
    c_fire: str = create_fire()
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{c_air}' and '{c_sp}' mixed with '{c_fire}'"
    )
