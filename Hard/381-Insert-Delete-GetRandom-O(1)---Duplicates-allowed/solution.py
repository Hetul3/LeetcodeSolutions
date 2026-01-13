class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        self.arr.append(val)
        if val not in self.map:
            self.map[val] = set()
            self.map[val].add(len(self.arr)-1)
            return True
        self.map[val].add(len(self.arr)-1)
        return False

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        if len(self.arr) == 1:
            self.arr = []
            self.map = {}
            return True
        num_at_end = self.arr[-1]
        index_of_removal = self.map[val].pop()
        if not self.map[val]:
            del self.map[val]
        if index_of_removal == len(self.arr)-1:
            self.arr = self.arr[:-1]
            return True
        self.arr[index_of_removal] = num_at_end
        self.map[num_at_end].remove(len(self.arr)-1)
        self.map[num_at_end].add(index_of_removal)
        self.arr = self.arr[:-1]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()