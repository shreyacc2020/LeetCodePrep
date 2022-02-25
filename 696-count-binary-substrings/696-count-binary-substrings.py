class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #00110011
        q = deque()
        output = 0
        for c in s:
            while q and q[-1] ==c and q[0] != c:
                q.pop()
            if q and q[-1] !=c :
                q.pop()
                output+=1
            q.appendleft(c)
        return output