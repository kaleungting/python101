class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        memo = {0: 0, 1: 1}

        for n in range(2, n+1):
            memo[n] = memo[n - 1] + memo[n - 2]
        return memo[n]
