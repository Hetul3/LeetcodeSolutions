class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions)+1)
        for i in range(len(questions) - 1, -1, -1):
            dp[i] = dp[i+1]
            val = questions[i][0]
            if (i+1+questions[i][1]) <= len(questions):
                val+=dp[i+1+questions[i][1]]
            dp[i] = max(dp[i], val)
        return dp[0]