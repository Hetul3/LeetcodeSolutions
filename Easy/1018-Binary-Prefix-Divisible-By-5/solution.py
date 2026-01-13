class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        sum = 0
        for i in nums:
            sum = (sum*2+i)%5
            if sum%5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result