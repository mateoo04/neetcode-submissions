class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_pool = 0
        while left < right:
            possible = min(heights[left], heights[right]) * (right - left)

            if possible > max_pool:
                max_pool = possible

            if heights[left] < heights[right]:
                left += 1
            else: right -= 1

        return max_pool