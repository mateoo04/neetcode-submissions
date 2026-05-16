class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            res = tuple(sorted(s))
            result[res].append(s)

        return list(result.values())

