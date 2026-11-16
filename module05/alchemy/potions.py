import elements
from .elements import create_air, create_earth


def healing_potion() -> str:
    e_el: str = create_earth()
    a_el: str = create_air()
    return f"Healing potion brewed with '{e_el}' and '{a_el}'"


def strength_potion() -> str:
    f_el: str = elements.create_fire()
    w_el: str = elements.create_water()
    return f"Strength potion brewed with '{f_el}' and '{w_el}'"
