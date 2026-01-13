class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        L = 0
        for i in range(len(s)):
            if s[i] == 'L':
                L+=1
            else:
                L-=1
            if L == 0:
                count+=1
        return count