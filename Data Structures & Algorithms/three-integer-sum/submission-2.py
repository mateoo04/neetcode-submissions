class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        result = set()
        sorted_nums = sorted(nums)
        left = 0
        while left < len(sorted_nums) - 2 and sorted_nums[left] <= 0:
            right = len(sorted_nums) - 1
            while left + 1 < right and sorted_nums[right] >= 0:
                possible_third = set(sorted_nums[left + 1:right])
                needed = (sorted_nums[left] + sorted_nums[right]) * -1
                if needed in possible_third:
                        to_add = (sorted_nums[left],sorted_nums[right], needed)
                        if to_add not in result: result.add(to_add)
                right -= 1
            left += 1

        return [list(item) for item in result]
        




