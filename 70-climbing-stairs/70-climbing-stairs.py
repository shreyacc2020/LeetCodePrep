class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        # if n == 2:
        #     return 2
        # elif n == 3:
        #     return 3
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one