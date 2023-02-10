import json
from dataclasses import dataclass


@dataclass
class Example:
    input: str
    output: list[str]


def load_data(path: str) -> list[Example]:
    with open(path, "rt") as f:
        return [Example(**json.loads(line)) for line in f]
