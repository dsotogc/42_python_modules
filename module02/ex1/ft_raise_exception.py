#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}ºC is too hot for plants (max 40ºC)")
    elif temp_int < 0:
        raise ValueError(f"{temp_int}ºC is too cold for plants (min 0ºC)")
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    data1: str = "25"
    print(f"Input data is \'{data1}\'")
    try:
        print(f"Temperature is now {input_temperature(data1)}ºC\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    data2: str = "abc"
    print(f"Input data is \'{data2}\'")
    try:
        print(f"Temperature is now {input_temperature(data2)}ºC\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    data3: str = "100"
    print(f"Input data is \'{data3}\'")
    try:
        print(f"Temperature is now {input_temperature(data3)}ºC\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    data4: str = "-50"
    print(f"Input data is \'{data4}\'")
    try:
        print(f"Temperature is now {input_temperature(data4)}ºC\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
