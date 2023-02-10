import bunkai
import sengiri


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
