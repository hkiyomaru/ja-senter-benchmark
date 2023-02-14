import logging
import pathlib

import bunkai
import hasami
import pysbd
import rhoknp
import sengiri
import spacy
from bunkai.cli import setup

here = pathlib.Path(__file__).parent


class Senter:
    def __call__(self, text: str) -> list[str]:
        raise NotImplementedError

    @property
    def name(self) -> str:
        raise NotImplementedError


class Rhoknp(Senter):
    """https://github.com/ku-nlp/rhoknp."""

    def __init__(self) -> None:
        self.senter = rhoknp.RegexSenter()

    def __call__(self, text: str) -> list[str]:
        return [s.text for s in self.senter(text).sentences]

    @property
    def name(self) -> str:
        return "rhoknp"


class Sengiri(Senter):
    """https://github.com/ikegami-yukino/sengiri."""

    def __call__(self, text: str) -> list[str]:
        return sengiri.tokenize(text)

    @property
    def name(self) -> str:
        return "sengiri"


class Hasami(Senter):
    """https://github.com/ikegami-yukino/sengiri."""

    def __call__(self, text: str) -> list[str]:
        return hasami.segment_sentences(text)

    @property
    def name(self) -> str:
        return "hasami"


class Bunkai(Senter):
    """https://github.com/megagonlabs/bunkai."""

    def __init__(self) -> None:
        model_path = here.joinpath("bunkai_model")
        if not model_path.exists():
            setup(here / "bunkai_model", None)
        self.bunkai = bunkai.Bunkai(path_model=model_path)

        # Disable verbose logging
        logging.getLogger("bunkai").setLevel(logging.ERROR)

    def __call__(self, text: str) -> list[str]:
        return list(self.bunkai(text))

    @property
    def name(self) -> str:
        return "bunkai"


class Pysbd(Senter):
    """https://github.com/ikegami-yukino/sengiri."""

    def __init__(self) -> None:
        self.seg = pysbd.Segmenter(language="ja")

    def __call__(self, text: str) -> list[str]:
        return self.seg.segment(text)

    @property
    def name(self) -> str:
        return "pysbd"


class Ginza(Senter):
    """https://github.com/megagonlabs/ginza."""

    def __init__(self) -> None:
        self.nlp = spacy.load("ja_ginza")  # standard model

    def __call__(self, text: str) -> list[str]:
        return [sent.text for sent in self.nlp(text).sents]

    @property
    def name(self) -> str:
        return "ginza"
