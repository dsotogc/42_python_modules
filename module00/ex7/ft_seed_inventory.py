def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    cptz_s_type: str = seed_type.capitalize()
    if unit == "packets":
        print(cptz_s_type, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(cptz_s_type, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(f"{cptz_s_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
