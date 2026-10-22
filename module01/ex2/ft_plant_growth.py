#!/usr/bin/env python3

class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0
        self.age_old: int = 0
        self.growth_rate: float = 1

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
    plant1 = Plant()
    total_growth: float = 0
    plant1.name = "Sunflower"
    plant1.height = 20
    plant1.age_old = 54
    plant1.growth_rate = 2.5
    print("=== Garden Plant Growth ===")
    plant1.show()
    print()
    for i in range(1, 8):
        print(f"=== Day {i} ==")
        plant1.age()
        total_growth += plant1.grow()
        plant1.show()
    print("\n=== Growth this week ===")
    print(f"{total_growth}cm")


if __name__ == "__main__":
    main()
