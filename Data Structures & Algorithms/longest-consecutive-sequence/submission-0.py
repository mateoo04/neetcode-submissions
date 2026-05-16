class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_count = 0
        for n in nums:
            count = 1
            if n - 1 not in numbers:
                add = n + 1
                while add in numbers:
                    count += 1
                    add += 1
                if count > max_count: max_count = count
        return max_count
            
        