#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    input_text: str = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        coords: list[str] = input(input_text).split(',')
        if len(coords) != 3:
            print("Invalid syntax")
            continue
        values: list[float] = []
        valid_cords: bool = True
        for coord in coords:
            try:
                values.append(float(coord.strip()))
            except ValueError as e:
                print(f"Error on parameter '{coord.strip()}': {e}")
                valid_cords = False
        if valid_cords:
            x, y, z = values
            return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    c1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {c1}")
    print(f"It includes: X={c1[0]}, Y={c1[1]}, Z={c1[2]}")
    to_center: float = math.sqrt(c1[0]**2 + c1[1]**2 + c1[2]**2)
    print(f"Distance to center: {to_center:.4f}")
    print()
    print("Get a second set of coordinates")
    c2: tuple[float, float, float] = get_player_pos()
    dist: float = math.sqrt(
        (c2[0] - c1[0])**2 + (c2[1] - c1[1])**2 + (c2[2] - c1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {dist:.4f}")


if __name__ == "__main__":
    main()
