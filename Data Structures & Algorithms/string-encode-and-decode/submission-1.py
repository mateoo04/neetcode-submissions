import functools

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) < 1: return "Ništa"
        return functools.reduce(lambda a, b: a + "|*|" + b, strs)

    def decode(self, s: str) -> List[str]:
        if s == "Ništa": return []
        return s.split("|*|")
