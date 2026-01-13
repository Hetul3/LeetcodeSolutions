class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result, match_set = set(), set()
        for i in range(len(s) - 9):
            curr_string = s[i:i+10]
            if curr_string in match_set:
                result.add(curr_string)
            match_set.add(curr_string)
        return list(result)