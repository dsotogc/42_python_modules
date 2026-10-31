#!/usr/bin/env python3

from typing import Generator
import random


def gen_event(
        players: list[str],
        actions: list[str]
) -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        yield event_list.pop(random.randint(0, len(event_list) - 1))


def main() -> None:
    print("=== Game Data Stream Processors ===")
    players: list[str] = ["Bob", "Alice", "Dylan", "Charlie"]
    actions: list[str] = [
        "Run", "Eat", "Sleep", "Grab",
        "Move", "Climb", "Swim"
    ]

    for i in range(0, 1000):
        ev: tuple[str, str] = next(gen_event(players, actions))
        print(f"Event {i}: Player {ev[0].lower()} did action {ev[1].lower()}")

    new_ev: list[tuple[str, str]] = []
    for _ in range(0, 10):
        new_ev.append(next(gen_event(players, actions)))
    print(f"Built list of 10 events: {new_ev}")

    for event in consume_event(new_ev):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {new_ev}")


if __name__ == "__main__":
    main()
