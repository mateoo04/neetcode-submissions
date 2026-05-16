class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j: r[j] *= nums[i]
        return r
        