class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""

        res = ""
        lst = self.keys[key]

        left = 0
        right = len(lst) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if lst[mid][1] <= timestamp:
                res = lst[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res