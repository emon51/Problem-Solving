#TLE_linerar_search.
class TimeMap:

    def __init__(self):
      self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
      if key not in self.map:
        self.map[key] = [[value, timestamp]]
      else:
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
      vals = self.map.get(key, []) 
      #print(vals)
      #linear search
      res = ""
      for i in range(len(vals)):
        if vals[i][1] <= timestamp:
          res = vals[i][0]
      return res
#========================================================================================#
#Binary_search
class TimeMap:

    def __init__(self):
        self.map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([value, timestamp])
        else:
            self.map[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map.get(key, [])
        #Here timestamps are setted in incresing(sorted) manner.
        res = ''
        l, r = 0, len(vals) -1
        while l <= r:
            mid = l + (r - l) // 2
            if vals[mid][1] <= timestamp:
                res = vals[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
