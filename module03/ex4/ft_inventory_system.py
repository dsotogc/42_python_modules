#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    program_name, *inv = sys.argv
    if (len(sys.argv) == 1):
        print("Error - No parameters received")
        print(f"Usage: python3 {program_name} item1:2 item2:42")
        return
    for arg in inv:
        arg_splited: list[str] = arg.split(':')
        if (len(arg_splited) != 2):
            if (len(arg_splited) == 1):
                print(f"Error - invalid parameter '{arg_splited[0]}'")
            else:
                print("Error - Invalid format\nUsage example: item:42")
        else:
            if (arg_splited[0] in inventory):
                print(f"Redundant item '{arg_splited[0]}' - discarding")
            else:
                try:
                    quantity: int = int(arg_splited[1])
                    if (quantity < 0):
                        print(f"Negative quantity error for {arg_splited[0]}")
                except ValueError as e:
                    print(f"Quantity error for '{arg_splited[0]}': {e}")
                    continue
                inventory.update({arg_splited[0]: quantity})

    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")
    total_sum: int = sum(inventory.values())
    print(
        f"Total quantity of the {len(inventory)} items: "
        f"{total_sum}"
    )
    most, least = "", ""
    for item in inventory:
        perc: float = round(inventory[item] * 100 / total_sum, 1)
        print(f"Item {item} represents {perc}%")
        if most == "" or inventory[item] > inventory[most]:
            most = item
        if least == "" or inventory[item] < inventory[least]:
            least = item
    print(f"Item most abundat: {most} with quantity {inventory[most]}")
    print(f"Item least abundat: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
