class Solution:
    def nextOne(self, s: str, index: int, num: int) -> int:
        while (index >= 0 and index < len(s)) and not ((ord(s[index]) >= ord('a') and ord(s[index]) <= ord('z')) or (ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'))):
            index += num
        return index

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True
        lowercased = s.lower()
        start = self.nextOne(lowercased, 0, 1)
        end = self.nextOne(lowercased, len(s) - 1, - 1)
        while start <= end:
            if lowercased[start] != lowercased[end]: return False
            start = self.nextOne(lowercased, start + 1, 1)
            end = self.nextOne(lowercased, end - 1, - 1)

        return True



