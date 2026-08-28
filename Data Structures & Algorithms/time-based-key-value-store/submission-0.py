class TimeMap:


    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None: 
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        values = self.keyStore[key]
        left = 0
        right = len(values) - 1
        best = ""
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                best = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return best