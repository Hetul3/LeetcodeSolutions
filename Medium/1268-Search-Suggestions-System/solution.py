class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() 
        result = []
        curr_index = 0
        for i in range(1, len(searchWord)+1): 
            substring = searchWord[:i] 
            sub_result = []
            temp_curr_index = curr_index
            while curr_index < len(products):
                if products[curr_index].find(substring) == 0:
                    sub_result.append(products[curr_index])
                    temp_curr_index = curr_index
                    if curr_index+1 < len(products):
                        word2 = products[(curr_index+1)%len(products)]
                        if word2.find(substring) == 0:
                            sub_result.append(word2)
                    if curr_index+2 < len(products):
                        word3 = products[(curr_index+2)%len(products)]
                        if word3.find(substring) == 0:
                            sub_result.append(word3)
                    break
                curr_index+=1
                temp_curr_index = curr_index
            curr_index = temp_curr_index
            result.append(sub_result)
        return result