#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self.name: str = name
        self._height: float = 0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f'{self.name}: Error, height can\'t be negative')
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f'{self.name}: Error, age can\'t be negative')
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, days: int, grow_rate: float) -> None:
        print(f"[make {self.name.lower()} grow and age for {days} days]")
        self.set_age(self.get_age() + days)
        self.set_height(self.get_height() + (days * grow_rate))

    def show(self) -> None:
        print(f"{self.name}: "
              f"{self.get_height(): .1f}cm, {self.get_age()} days old")


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float = 0,
            age: int = 0,
            color: str = "unknown"
    ) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def get_color(self) -> str:
        return self._color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.get_color().lower()}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float = 0,
            age: int = 0,
            trunk_diameter: float = 0
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height: .1f}cm long and "
              f"{self._trunk_diameter: .1f}cm wide.")

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.get_trunk_diameter(): .1f}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float = 0,
            age: int = 0,
            harvest_season: str = "Unknown"
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def set_nutritional_value(self, value: int) -> None:
        self._nutritional_value = value

    def grow(self, days: int, grow_rate: float = 2.1) -> None:
        super().grow(days, grow_rate)
        self.set_nutritional_value(days)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "Red")
    flower.show()
    print("[asking the flower to bloom]")
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5, 10, "April")
    vegetable.show()
    vegetable.grow(20)
    vegetable.show()


if __name__ == "__main__":
    main()
