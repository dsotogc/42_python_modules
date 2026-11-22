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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for proc in self.processors:
                if proc.validate(item):
                    try:
                        proc.ingest(item)
                    except (ValueError, TypeError) as error:
                        print(f"DataStream error - {error}")
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{item}"
                )

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        for proc in self.processors:
            remaining = len(proc.values)
            total = remaining + proc.n_outputs
            name = proc.__class__.__name__.removesuffix("Processor")
            print(
                f"{name} Processor: total {total} items processed, "
                f"remaining {remaining} on processor"
            )
        if len(self.processors) == 0:
            print("No processor found, no data")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print()

    print("Registering Numeric Processor")
    np = NumericProcessor()
    ds.register_processor(np)
    print()

    data_batch: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {data_batch}")
    ds.process_stream(data_batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(tp)
    ds.register_processor(lp)
    print("Send the same batch again")
    ds.process_stream(data_batch)
    ds.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for proc, count in [(np, 3), (tp, 2), (lp, 1)]:
        for _ in range(count):
            print(f"{proc.__class__.__name__}: {proc.output()}")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
