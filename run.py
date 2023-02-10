import json
import logging
import time
from dataclasses import dataclass
from pathlib import Path

from senters import Bunkai, Ginza, Sengiri, Senter

logger = logging.getLogger(__name__)

here = Path(__file__).parent

data_dir = here.joinpath("data")


@dataclass
class Example:
    input: str
    output: list[str]


def benchmark(senter: Senter, examples: list[Example]) -> None:
    """Perform benchmarking.

    Args:
        senter: A sentence segmentation tool to be tested.
        examples: Examples used for benchmarking.
    """
    start = time.time()
    predictions = [senter(example.input) for example in examples]
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
    f1 = 100 * 2 * pre * rec / (pre + rec)
    print(f"{senter.name}\t{f1:5.1f} (Elapsed time: {elapsed_time:.2f})")


def main() -> None:
    for data_file in data_dir.glob("*.jsonl"):
        print("#", data_file.absolute())
        with data_file.open() as f:
            examples = [Example(**json.loads(line)) for line in f]
        benchmark(Sengiri(), examples)
        benchmark(Bunkai(), examples)
        benchmark(Ginza(), examples)
        print("---")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    main()
