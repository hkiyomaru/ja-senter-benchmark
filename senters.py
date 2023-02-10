import sengiri


class Senter:
    def __call__(self, text: str) -> list[str]:
        raise NotImplementedError


class Sengiri(Senter):
    def __call__(self, text: str) -> list[str]:
        return sengiri.tokenize(text)
