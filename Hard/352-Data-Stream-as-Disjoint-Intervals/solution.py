class SummaryRanges:

    def __init__(self):
        self.max_num = 0
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)
        self.max_num = max(self.max_num, value)

    def getIntervals(self) -> List[List[int]]:
        result = []
        curr = None
        for i in range(self.max_num+2):
            if i in self.nums and curr == None:
                curr = [i, i]
            elif curr and i in self.nums:
                curr[1] = i
            elif curr and i not in self.nums:
                result.append(curr)
                curr = None
        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()