class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum = 0
        index = {}
        for i in range(len(nums)):
            sum = (sum+nums[i])%k
            if sum == 0 and i != 0:
                return True
            if sum in index:
                if index[sum] < i-1:
                    return True
            else:
                index[sum] = i
        return False