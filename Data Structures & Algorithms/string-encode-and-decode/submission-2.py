import functools

class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""

        for s in strs:
            r += str(len(s)) + "#" + s

        return r

    def decode(self, s: str) -> List[str]:
        r = []
        i = s.find("#")
        end = 0
        while i != -1:
            start = int(s[end:i])
            end = int(i + start + 1)
            text = s[i + 1 : end]
            r.append(text)
            i = s.find("#", end)
        
        return r
            



