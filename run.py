import logging
from pathlib import Path

from benchmark import Result, get_benchmark, summarize_results
from senters import Bunkai, Ginza, Sengiri
from utils import load_data

logger = logging.getLogger(__name__)

here = Path(__file__).parent

data_dir = here.joinpath("data")


def main() -> None:
    results: dict[str, dict[str, Result]] = {}
    for data_file in data_dir.glob("*.jsonl"):
        logger.info(f"Start benchmarking on '{data_file.absolute()}'.")
        examples = load_data(str(data_file))
        logger.info(f"Number of examples: {len(examples):,}")

        results[str(data_file)] = {}

        # sengiri
        results[str(data_file)]["sengiri"] = get_benchmark(Sengiri(), examples)
        # bunkai
        results[str(data_file)]["bunkai"] = get_benchmark(Bunkai(), examples)
        # ginza
        results[str(data_file)]["ginza"] = get_benchmark(Ginza(), examples)

    for data_name, result in results.items():
        print(f"Benchmark on {data_name}")
        summarize_results(result)
        print("---")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    main()
