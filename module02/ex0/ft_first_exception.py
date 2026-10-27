#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    data1: str = "25"
    print(f"Input data is \'{data1}\'")
    try:
        print(f"Temperature is now {input_temperature(data1)}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    data2: str = "abc"
    print(f"Input data is \'{data2}\'")
    try:
        print(f"Temperature is now {input_temperature(data2)}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
