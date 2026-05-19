from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.mapping[key]) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            if self.mapping[key][mid][1] <= timestamp:
                l = mid + 1
                result = self.mapping[key][mid][0]
            else:
                r = mid - 1
        return result

