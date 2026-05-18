class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_outer = 0
        high_outer = len(matrix) - 1
        while low_outer <= high_outer:
            mid_outer = (low_outer + high_outer) // 2
            if matrix[mid_outer][0] == target: return True
            elif target < matrix[mid_outer][0]:
                high_outer = mid_outer - 1
            else:
                if matrix[mid_outer][-1] < target:
                    low_outer = mid_outer + 1
                else:
                    low_inner = 1
                    high_inner = len(matrix[mid_outer]) - 1

                    while low_inner <= high_inner:
                        mid_inner = (low_inner + high_inner) // 2
                        if target == matrix[mid_outer][mid_inner]: return True
                        elif target < matrix[mid_outer][mid_inner]:
                            high_inner = mid_inner - 1
                        else: low_inner = mid_inner + 1
                    return False
        return False