class TimeMap:
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key not present, initialize
        if key not in self.dict:
            self.dict[key] = []
        # Just append since timestamps are always increasing
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        
        arr = self.dict[key]  # list of [timestamp, value]
        
        # Manual binary search (no inbuilt)
        left, right = 0, len(arr) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]   # candidate answer
                left = mid + 1      # try to find later timestamp
            else:
                right = mid - 1
        return res
