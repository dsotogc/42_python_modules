#!/usr/bin/env python3

import random


def gen_player_achievements(achivements: list[str], num: int) -> set[str]:
    return set(random.sample(achivements, num))


def main() -> None:
    ach: list[str] = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer',
    ]

    p1: set[str] = gen_player_achievements(ach, random.randint(1, len(ach)))
    p2: set[str] = gen_player_achievements(ach, random.randint(1, len(ach)))
    p3: set[str] = gen_player_achievements(ach, random.randint(1, len(ach)))
    p4: set[str] = gen_player_achievements(ach, random.randint(1, len(ach)))

    print("=== Achivement Tracker System ===\n")

    print(f"Player Alice: {p1}")
    print(f"Player Bob: {p2}")
    print(f"Player Charlie: {p3}")
    print(f"Player Dylan: {p4}")

    print(f"\nAll distinct achievements: {p1.union(p2, p3, p4)}")

    print(f"\nCommon achievements: {p1.intersection(p2, p3, p4)}")

    print(f"\nOnly Alice has: {p1.difference(p2, p3, p4)}")
    print(f"Only Bob has: {p2.difference(p1, p3, p4)}")
    print(f"Only Charlie has: {p3.difference(p2, p1, p4)}")
    print(f"Only Dylan has: {p4.difference(p2, p3, p1)}")

    print(f"\nAlice is missing: {set(ach).difference(p1)}")
    print(f"Bob is missing: {set(ach).difference(p2)}")
    print(f"Charlie is missing: {set(ach).difference(p3)}")
    print(f"Dylan is missing: {set(ach).difference(p4)}")


if __name__ == "__main__":
    main()
