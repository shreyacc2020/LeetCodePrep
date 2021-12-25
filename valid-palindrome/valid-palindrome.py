class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # print(s)
        punctuation = "!\'\" #$%&'()*+,-./:;<=>?@[\]^_`{|}~.\""
        for character in punctuation:
            s = s.replace(character, '')
        # s = s.strip(" ")
        j = len(s)-1
        sReverse = []
        while j>=0:
            sReverse.append(s[j])
            j-=1
        sReverse = "".join(sReverse)
        print(s)
        if s == sReverse:
            return True
        else:
            return False