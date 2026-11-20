from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self):
        self.values: list[Any] = []
        self.n_outputs: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        self.n_outputs += 1
        return (self.n_outputs - 1, self.values.pop(0))


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, (int, float, list)):
            return False
        if isinstance(data, list):
            return all(isinstance(n, (int, float)) for n in data)
        return True

    def ingest(self, data: int | float | list[int | float]):
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

    def ingest(self, data: int | float | list[int | float]):
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
            return all(isinstance(k, str) and isinstance(v, str) for k, v in data.items())
        if isinstance(data, list):
            return all(
                isinstance(log, dict)
                and all(isinstance(k, str) and isinstance(v, str) for k, v in log.items())
                for log in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]):
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for l in data:
                self.values.append(str(l))
        else:
            self.values.append(str(data))


class DataStream:
    def __init__(self):
        self.processors: list[DataProcessor] = []
        self.total_items: int = 0

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            validated: bool = False
            self.total_items += 1
            for proc in self.processors:
                if proc.validate(item):
                    validated = True
                    proc.ingest(item)
            if not validated:
                print(
                    f"DataStream error - Can't process element in stream: {stream}")

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        for proc in self.processors:
            print(f"{proc.__class__.__name__}: {len(proc.values)} items processed, "
                  f"remaining {self.total_items - len(proc.values)} on processor")
        if len(self.processors) == 0:
            print("No processor found, no data")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print()

    print("Registering Numeric Processor")
    ds.register_processor(NumericProcessor())
    print()

    data_batch: list[Any] = ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message': 'Telmet access! Use ssh instead'}, {
        'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data_batch}")
    ds.process_stream(data_batch)
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
