# Last Updated: 5/15/2026, 11:14:29 PM
class Solution:
    def fib(self, n: int,memo={}) -> int:
        if n<2:
            return n
        if n not in memo:
            memo[n]=self.fib(n-1,memo)+self.fib(n-2,memo)
        return memo[n]
        