class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map[key]
        if not arr or arr[0][1] > timestamp:
            return ""
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r-l)//2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            if arr[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid
        return arr[l - 1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)