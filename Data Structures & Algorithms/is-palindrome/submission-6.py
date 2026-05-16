import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        redone = re.sub(r"[^a-zA-Z0-9]","", s).lower()
        print("here: ", redone)
        for i in range(len(redone)//2):
            if redone[i] != redone[-i-1]: return False

        return True