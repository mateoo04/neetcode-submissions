class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                popped = stack.pop()
                result[popped[1]] = i - popped[1]
            stack.append((temperatures[i], i))
        return result
        