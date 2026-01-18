class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def is_magic_square(x, y, k):
            maintain_sum = 0
            for i in range(x, x+k):
                maintain_sum+=grid[i][y]
            for i in range(x, x+k):
                curr_sum = 0
                for j in range(y, y+k):
                    curr_sum+=grid[i][j]
                if curr_sum != maintain_sum:
                    return False
            for j in range(y, y+k):
                curr_sum = 0
                for i in range(x, x+k):
                    curr_sum+=grid[i][j]
                if curr_sum != maintain_sum:
                    return False
            curr_sum1, curr_sum2 = 0, 0
            for i in range(k):
                curr_sum1+=grid[x+i][y+i]
                curr_sum2+=grid[x+i][y+k-i-1]
            if curr_sum1 != maintain_sum or curr_sum2 != maintain_sum:
                return False
            return True
            

        max_side_length = 1
        max_possible_size = min(len(grid), len(grid[0]))
        for k in range(1, max_possible_size+1):
            for i in range(len(grid) - k + 1):
                for j in range(len(grid[i]) - k + 1):
                    if is_magic_square(i, j, k):
                        max_side_length = k
                        break
                if max_side_length == k:
                    break
        return max_side_length