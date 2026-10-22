#!/usr/bin/env python3

class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0
        self.age: int = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def main() -> None:
    plant1 = Plant()
    plant2 = Plant()
    plant3 = Plant()
    plant1.name = "Rose"
    plant2.name = "Sunflower"
    plant3.name = "Cactus"
    plant1.height = 25.5
    plant2.height = 80
    plant3.height = 15
    plant1.age = 30
    plant2.age = 45
    plant3.age = 120
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
