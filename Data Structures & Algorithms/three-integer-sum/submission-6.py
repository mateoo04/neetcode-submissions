class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        s_nums = sorted(nums)
        result = []
        for i in range(len(s_nums) - 2):
            if i > 0 and s_nums[i] == s_nums[i - 1]: continue
            if s_nums[i] > 0: break
            
            left = i + 1
            right = len(s_nums) - 1

            while left < right:
                total = s_nums[i] + s_nums[left] + s_nums[right]
                if total == 0:
                    result.append([s_nums[i], s_nums[left], s_nums[right]])
                    left += 1
                    right -= 1

                    while left < right and s_nums[left] == s_nums[left - 1]:
                        left += 1

                    while left < right and s_nums[right] == s_nums[right + 1]:
                        right -= 1

                elif total < 0 and left < len(s_nums) - 1:
                    left += 1
                elif total > 0 and right > left:
                    right -= 1
        return result