class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        result = []
        pairs = 0
        for q in queries:
            index, new_color = q[0], q[1]
            change_of_pairs = 0
            if index > 0:
                if colors[index-1] != 0 and colors[index] == colors[index-1] and new_color != colors[index-1]:
                    change_of_pairs-=1
                if colors[index-1] != 0 and colors[index] != colors[index-1] and new_color == colors[index-1]:
                    change_of_pairs+=1
            if index < n-1:
                if colors[index+1] != 0 and colors[index] == colors[index+1] and new_color != colors[index+1]:
                    change_of_pairs-=1
                if colors[index+1] != 0 and colors[index] != colors[index+1] and new_color == colors[index+1]:
                    change_of_pairs+=1
            pairs+=change_of_pairs
            result.append(pairs)
            colors[index] = new_color
        return result