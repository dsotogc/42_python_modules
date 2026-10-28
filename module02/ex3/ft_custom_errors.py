#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: str) -> None:
        super().__init__(f"The {plant.lower()} is wilting!")


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def test_plant_error(plant_type: str, is_healthy: bool) -> None:
    if not is_healthy:
        raise PlantError(plant_type)


def test_water_error(water_level: int) -> None:
    if water_level < 10:
        raise WaterError()


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        test_plant_error("Tomato", False)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        test_water_error(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        test_plant_error("Tomato", False)
        test_water_error(2)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        test_water_error(2)
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
