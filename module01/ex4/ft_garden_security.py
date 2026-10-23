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
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: "
              f"{self._height: .1f}cm, {self._age} days old")


def main() -> None:
    print(" === Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-2)
    plant.set_age(-15)
    print()
    plant.show()


if __name__ == "__main__":
    main()
