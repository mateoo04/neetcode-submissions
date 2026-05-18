import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        final_k = right
        while left <= right:
            possible_h = 0
            mid = (left + right) // 2
            for pile in piles:
                possible_h += math.ceil(pile / mid)

            if possible_h <= h:
                final_k = mid
                right = mid - 1
            else:
                left = mid + 1
        return final_k


        