class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.mem_arr = [] # (start, size, mID)

    def allocate(self, size: int, mID: int) -> int:
        if len(self.mem_arr) == 0:
            if size <= self.n:
                self.mem_arr.append((0, size, mID))
                return 0
            else:
                return -1
        curr_start = 0
        for i in range(len(self.mem_arr)):
            block_size = self.mem_arr[i][0] - curr_start
            if block_size >= size:
                self.mem_arr.append((curr_start, size, mID))
                self.mem_arr.sort()
                return curr_start
            else:
                curr_start = self.mem_arr[i][0] + self.mem_arr[i][1]
        if curr_start + size <= self.n:
            self.mem_arr.append((curr_start, size, mID))
            self.mem_arr.sort()
            return curr_start
        return -1

    def freeMemory(self, mID: int) -> int:
        total_freed = 0
        for i in range(len(self.mem_arr)-1,-1,-1):
            if self.mem_arr[i][2] == mID:
                total_freed+=self.mem_arr[i][1]
                self.mem_arr.pop(i)
        self.mem_arr.sort()
        return total_freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)