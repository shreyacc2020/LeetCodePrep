class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        set = []
        for i in range(0,len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in map:
                if map[c1] != c2:
                    return False
            elif (c1 not in map and c2 in set):
                return False
            else:
                map[c1] = c2
                set.append(c2)
        return True
            