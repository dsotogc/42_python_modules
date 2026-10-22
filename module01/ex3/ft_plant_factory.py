#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age_old: int,
            growth_rate: float = 1
    ) -> None:
        self.name: str = name
        self.height: float = height
        self.age_old: int = age_old
        self.growth_rate: float = growth_rate

    def age(self) -> None:
        self.age_old += 1

    def grow(self) -> float:
        self.height += self.growth_rate
        return self.growth_rate

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age_old} days old"
        )


def main() -> None:
    plants = [
        Plant("Sunflower", 80, 45, 2.5),
        Plant("Rose", 25, 30),
        Plant("Cactus", 10.3, 45, 0.5),
        Plant("Oak", 200, 320, 0.03),
        Plant("Fern", 15, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
