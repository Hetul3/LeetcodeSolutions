class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors
        i, j = 0, 0
        result = 0

        while j < len(colors)//2:
            if i-j < k-1:
                j = i
                while i < j+k-1:
                    i+=1
                    if colors[i] == colors[i-1]:
                        break
            elif colors[i] != colors[i-1]:
                result+=1
                i+=1
                j+=1
            else:
                j = i
        return result