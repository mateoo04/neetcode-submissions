class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif len(stack) > 0:
                if stack.pop() != mapping[i]: return False
            else: return False

        return len(stack) == 0
        