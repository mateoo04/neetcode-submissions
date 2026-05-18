class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                result[popped] = i - popped
            stack.append(i)
        return result