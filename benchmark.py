import time
from dataclasses import dataclass

from senters import Senter
from utils import Example


@dataclass
class Result:
    f1: float
    elapsed_time: float


def get_benchmark(senter: Senter, examples: list[Example]) -> Result:
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
    precicion = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 100 * 2 * precicion * recall / (precicion + recall)

    return Result(f1, elapsed_time)


def summarize_results(results: dict[str, Result]) -> None:
    print("Senter\tF1\tElapsed Time")
    for name, result in results.items():
        print(f"{name}\t{result.f1:.1f}\t{result.elapsed_time:.2f}")
