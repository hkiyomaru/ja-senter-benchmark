import json
import logging
import time
from dataclasses import dataclass
from pathlib import Path

from senters import Bunkai, Ginza, Hasami, Kuzukiri, Pysbd, Rhoknp, Sengiri, Senter

logger = logging.getLogger(__name__)

here = Path(__file__).parent

data_dir = here.joinpath("data")


def post_process(sents: list[str]) -> list[str]:
    return [sent.strip() for sent in sents if sent.strip()]


@dataclass
class Example:
    input: str
    output: list[str]

    def __post_init__(self) -> None:
        self.output = post_process(self.output)


def benchmark(senter: Senter, examples: list[Example]) -> None:
    """Perform benchmarking.

    Args:
        senter: A sentence segmentation tool to be tested.
        examples: Examples used for benchmarking.
    """
    start = time.time()
    predictions = []
    for example in examples:
        prediction = post_process(senter(example.input))
        predictions.append(prediction)
    end = time.time()

    # Get elapsed time
    elapsed_time = end - start

    # Calculate F1 (micro-average)
    tp, fp, fn = 0, 0, 0
    for prediction, example in zip(predictions, examples):
        output = example.output
        tp += sum(p in output for p in prediction)
        fp += sum(p not in output for p in prediction)
        fn += sum(o not in prediction for o in output)
    pre = tp / (tp + fp)
    rec = tp / (tp + fn)
    if pre + rec > 0:
        f1 = 100 * 2 * pre * rec / (pre + rec)
    else:
        f1 = 0.0
    print(f"{senter.name}\t{f1:5.1f} (Elapsed time: {elapsed_time:.2f})")


def main() -> None:
    senter_list = [
        Rhoknp(),
        Sengiri(),
        Hasami(),
        Kuzukiri(),
        Pysbd(),
        Bunkai(),
        Ginza(),
    ]
    for data_file in data_dir.glob("*.jsonl"):
        print("#", data_file.absolute())
        with data_file.open() as f:
            examples = [Example(**json.loads(line)) for line in f]
        for senter in senter_list:
            benchmark(senter, examples)
        print("---")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    main()
