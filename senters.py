import bunkai
import sengiri
import spacy


class Senter:
    def __call__(self, text: str) -> list[str]:
        raise NotImplementedError


class Sengiri(Senter):
    """https://github.com/ikegami-yukino/sengiri."""

    def __call__(self, text: str) -> list[str]:
        return sengiri.tokenize(text)


class Bunkai(Senter):
    """https://github.com/megagonlabs/bunkai."""

    def __init__(self) -> None:
        self.bunkai = bunkai.Bunkai()

    def __call__(self, text: str) -> list[str]:
        return list(self.bunkai(text))


class Ginza(Senter):
    """https://github.com/megagonlabs/ginza."""

    def __init__(self) -> None:
        self.nlp = spacy.load("ja_ginza")  # standard model

    def __call__(self, text: str) -> list[str]:
        return [sent.text for sent in self.nlp(text).sents]
