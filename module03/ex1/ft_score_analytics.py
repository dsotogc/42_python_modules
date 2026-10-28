#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argc: int = len(sys.argv)
    scores: list[int] = []
    if argc >= 1:
        i: int = 1
        while i < argc:
            try:
                new_score: int = int(sys.argv[i])
                scores.append(new_score)
            except ValueError:
                print(f"Invalid parameter: \'{sys.argv[i]}\'")
            finally:
                i += 1
    if len(scores) == 0:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {(sum(scores) / len(scores)): .1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
