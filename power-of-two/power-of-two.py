import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            product = 1
            while product<n:
                product*=2
            if product == n:
                return True
            else:
                return False