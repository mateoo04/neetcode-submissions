class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(len(nums)):
            prefix[i] = (prefix[i - 1] if i > 0 else 1) * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = (suffix[i + 1] if i < len(nums) - 1 else 1) * nums[i]

        result = []
        for i in range(len(nums)):
            result.append((prefix[i - 1] if i > 0 else 1) * (suffix[i + 1] if i < len(nums) - 1 else 1))

        return result

        