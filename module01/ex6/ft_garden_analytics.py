#!/usr/bin/env python3


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def get_grow_calls(self) -> int:
            return self._grow_calls

        def get_age_calls(self) -> int:
            return self._age_calls

        def get_show_calls(self) -> int:
            return self._show_calls

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self.name: str = name
        self._height: float = 0
        self._age: int = 0
        self._stats: Plant._Stats = self._Stats()
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> "Plant._Stats":
        return self._stats

    def grow(self, amount: float = 1) -> None:
        self._stats.record_grow()
        self.set_height(self._height + amount)

    def age(self, days: int = 1) -> None:
        self._stats.record_age()
        self.set_age(self._age + days)

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self.name}: "
              f"{self.get_height():.1f}cm, {self.get_age()} days old")

    @staticmethod
    def older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant")


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

    def is_bloomed(self) -> bool:
        return self._bloomed

    def get_color(self) -> str:
        return self._color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.get_color().lower()}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float = 0,
        age: int = 0,
        color: str = "unknown"
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = 0

    def set_seeds(self, seeds: int) -> None:
        if self.is_bloomed() and seeds >= 0:
            self._seeds = seeds

    def get_seeds(self) -> int:
        return self._seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def get_shade_calls(self) -> int:
            return self._shade_calls

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    _stats: _Stats

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
        self._stats.record_shade()
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide.")

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.get_trunk_diameter():.1f}cm")


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

    def grow(self, amount: float = 1) -> None:
        super().grow(amount)
        self.set_nutritional_value(self._nutritional_value + int(amount))

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.get_stats().display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    for days in (30, 400):
        print(f"Is {days} days more than a year? -> "
              f"{Plant.older_than_year(days)}")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "Red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "Yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.set_seeds(42)
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
