class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mapping = {}
        for i in range(len(s)):
            mapping[s[i]] = mapping.get(s[i],0) + 1
            mapping[t[i]] = mapping.get(t[i],0) - 1

        for num in mapping.values():
            if num != 0: return False
        return True


        