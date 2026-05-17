class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                match stack.pop():
                    case "(":
                        if i != ")": return False
                    case "[":
                        if i != "]": return False
                    case "{":
                        if i != "}": return False

        return len(stack) == 0
        