class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word_list = list(word)
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        for i in range(len(word_list)):
            if word_list[i] in alphabet:
                word_list[i] = " "
        word = ("".join(word_list))
        return (len(set(map(int, word.split()))))