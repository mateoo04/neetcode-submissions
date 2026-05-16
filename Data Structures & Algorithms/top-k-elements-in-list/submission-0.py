class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}

        for n in nums:
            mapping[n] = mapping.get(n, 0) + 1

        return sorted(mapping, key=lambda k: mapping[k], reverse=True)[:k]
        