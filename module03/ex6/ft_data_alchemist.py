#!/usr/bin/env python3

import random


def main() -> None:
    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"
    ]
    all_cap: list[str] = [name.capitalize() for name in players]
    only_cap: list[str] = [nam for nam in players if nam == nam.capitalize()]

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_cap}")
    print(f"New list of capitalized names only: {only_cap}")

    scores: dict[str, int] = {name: random.randint(0, 999) for name in all_cap}
    average: float = sum(scores.values()) / len(scores)
    print(f"Score dict: {scores}")
    print(f"Score average: {average: .2f}")

    h_scores: dict[str, int] = {n: s for n, s in scores.items() if s > average}
    print(f"High scores: {h_scores}")


if __name__ == "__main__":
    main()
