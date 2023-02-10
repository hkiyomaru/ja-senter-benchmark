import logging
from pathlib import Path

from benchmark import get_benchmark
from senters import Bunkai, Ginza, Sengiri
from utils import load_data

logger = logging.getLogger(__name__)

here = Path(__file__).parent

data_dir = here.joinpath("data")


def main() -> None:
    for data_file in data_dir.glob("*.jsonl"):
        print("#", data_file.absolute())
        examples = load_data(str(data_file))
        get_benchmark(Sengiri(), examples)
        get_benchmark(Bunkai(), examples)
        get_benchmark(Ginza(), examples)
        print("---")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    main()
