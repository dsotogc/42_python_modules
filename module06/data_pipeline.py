from typing import Any, Protocol
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
        logs = data if isinstance(data, list) else [data]
        for log in logs:
            if "log_level" in log and "log_message" in log:
                self.values.append(
                    f"{log['log_level']}: {log['log_message']}"
                )
            else:
                self.values.append(str(log))


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class ExportPluginCSV:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result: list[str] = []
        for _, content in data:
            result.append('"' + content.replace('"', '""') + '"')
        print(f"CSV Output:\n{','.join(result)}")


class ExportPluginJSON:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result: list[str] = []
        for idx, content in data:
            content = content.replace('\\', '\\\\').replace('"', '\\"')
            for code in range(32):
                content = content.replace(chr(code), f'\\u{code:04x}')
            result.append(f'"item_{idx}": "{content}"')
        print(f"JSON Output:\n{{{', '.join(result)}}}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb < 0:
            raise ValueError("Output count must not be negative")
        for proc in self.processors:
            data: list[tuple[int, str]] = []
            for _ in range(min(nb, len(proc.values))):
                data.append(proc.output())
            plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
    ds = DataStream()
    ds.print_processors_stats()
    print()

    print("Registering Processors")
    tp = TextProcessor()
    lp = LogProcessor()
    np = NumericProcessor()

    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)

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
    print(f"Send first batch of data on stream: {data_batch}\n")
    ds.process_stream(data_batch)
    ds.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, ExportPluginCSV())
    print()
    ds.print_processors_stats()

    data_batch2: list[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        list((32, 42, 64, 84, 128, 168)),
        'World hello'
    ]
    print(f"\nSend another batch of data: {data_batch2}")
    print()
    ds.process_stream(data_batch2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, ExportPluginJSON())
    print()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
