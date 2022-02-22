class Solution:
    def fib(self, n: int) -> int:
        result = 0
        # Default case
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # Recursive case
        elif n > 1:
            result = result + self.fib(n-1) + self.fib(n-2)
        return result