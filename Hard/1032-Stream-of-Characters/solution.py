class StreamChecker:

    def __init__(self, words: List[str]):
        self.subwords = set()
        self.words = set()
        self.max_word_length = 0
        for word in words:
            self.max_word_length = max(self.max_word_length, len(word))
            reverse_word = word[::-1]
            self.words.add(reverse_word)
            for i in range(len(reverse_word)):
                self.subwords.add(reverse_word[:i+1])
        self.full_word_reverse = ""
    def query(self, letter: str) -> bool:
        self.full_word_reverse = letter + self.full_word_reverse
        self.full_word_reverse = self.full_word_reverse[:self.max_word_length]
        for i in range(len(self.full_word_reverse)):
            subword = self.full_word_reverse[:i+1]
            if subword not in self.subwords:
                return False
            if subword in self.words:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)