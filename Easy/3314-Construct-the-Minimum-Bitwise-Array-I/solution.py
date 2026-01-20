class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            num = nums[i]
            for j in range(num):
                if j | (j+1) == num:
                    result.append(j)
                    break
            if len(result) == i:
                result.append(-1)
        return result