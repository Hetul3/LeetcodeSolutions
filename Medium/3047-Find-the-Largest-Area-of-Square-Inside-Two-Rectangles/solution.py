class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_result = 0
        for i in range(len(bottomLeft)):
            for j in range(i+1, len(bottomLeft)):
                rect1 = [bottomLeft[i], topRight[i]]
                rect2 = [bottomLeft[j], topRight[j]]
                if rect1[1][0] <= rect2[0][0] or rect1[1][1] <= rect2[0][1] or rect2[1][0] <= rect1[0][0] or rect2[1][1] <= rect1[0][1]:
                    continue
                intersection = [max(rect1[0][0], rect2[0][0]), max(rect1[0][1], rect2[0][1]), min(rect1[1][0], rect2[1][0]), min(rect1[1][1], rect2[1][1])]
                max_side_length = min(abs(intersection[2] - intersection[0]), abs(intersection[3] - intersection[1]))
                max_result = max(max_result, max_side_length)
        return max_result*max_result