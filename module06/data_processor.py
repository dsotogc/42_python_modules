from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.values: list[str] = []
        self.n_outputs: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        value = self.values.pop(0)
        self.n_outputs += 1
        return (self.n_outputs - 1, value)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, (int, float, list)):
            return False
        if isinstance(data, list):
            return all(isinstance(n, (int, float)) for n in data)
        return True

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for d in data:
                self.values.append(str(d))
        else:
            self.values.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, (str, list)):
            return False
        if isinstance(data, list):
            return all(isinstance(s, str) for s in data)
        return True

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for t in data:
                self.values.append(t)
        else:
            self.values.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(log, dict)
                and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in log.items()
                )
                for log in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for log in data:
                self.values.append(str(log))
        else:
            self.values.append(str(data))


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest('foo')
    except ValueError as e:
        print(f"Got exception: {e}")
    test_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {test_data}")
    np.ingest(test_data)
    print("Extracting 3 values...")
    for i in range(0, 3):
        result: tuple[int, str] = np.output()
        print(f"Numeric value: {result[0]}: {result[1]}")

    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    test_data2: list[str] = ["Hello", "Nexus", "World"]
    print(f"Trying to validate input {test_data2}: {tp.validate(test_data2)}")
    print(f"Processing data: {test_data2}")
    tp.ingest(test_data2)
    print("Extracting 1 value...")
    result = tp.output()
    print(f"Text value {result[0]}: {result[1]}")

    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    test_data3: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized!!'}
    ]
    print(f"Trying to validate input {test_data3}: {lp.validate(test_data3)}")
    print(f"Processing data: {test_data3}")
    lp.ingest(test_data3)
    print("Extracting 2 values...")
    for i in range(0, 2):
        result = lp.output()
        print(f"Log entry {result[0]}: {result[1]}")


if __name__ == "__main__":
    main()
