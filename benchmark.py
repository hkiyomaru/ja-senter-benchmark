import time

from senters import Senter
from utils import Example


def get_benchmark(senter: Senter, examples: list[Example]) -> None:
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
    print(f"{senter.name}\t{f1:5.1f} (Elapsed time: {elapsed_time:.2f})")
