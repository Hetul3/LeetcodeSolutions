class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        arr = [] # (list(words), whitespaces)
        temp_arr = []
        curr_chars = 0
        for word in words:
            char_available = maxWidth - curr_chars
            if len(word) <= char_available:
                curr_chars+=len(word)+1
                temp_arr.append(word)
            else:
                arr.append((temp_arr.copy(), maxWidth - curr_chars + len(temp_arr)))
                temp_arr = [word]
                curr_chars = len(word)+1
        result = []
        for i in range(len(arr)):
            word_list = arr[i][0]
            whitespaces = arr[i][1]
            if len(word_list) == 1:
                for j in range(whitespaces):
                    word_list[0]+=" "
                result.append(word_list[0])
            else:
                for j in range(len(word_list) - 1):
                    amount_to_add = whitespaces//(len(word_list)-1)
                    amount_to_add = amount_to_add+1 if whitespaces%(len(word_list) - 1) - 1 >= j else amount_to_add
                    for k in range(amount_to_add):
                        word_list[j]+=" "
                result.append("".join(word_list))
        if temp_arr:
            final_str = " ".join(temp_arr)
            while len(final_str) != maxWidth:
                final_str+=" "
            result.append(final_str)
        return result