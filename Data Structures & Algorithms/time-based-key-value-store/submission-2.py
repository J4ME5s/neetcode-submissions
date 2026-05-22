class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = []
        self.mapping[key].append((timestamp, value))
        


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        
        arr = self.mapping[key]
        
        l, r = 0, len(arr) - 1
        target = ""
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                target = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return target
        
