# Last Updated: 5/15/2026, 11:15:12 PM
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        def is_prime(n):
            return all((n % i) for i in range(2, int(n**0.5) + 1)) if n > 1 else False
        for i in range(left,right+1):
            num = (bin(i)[2:]).count('1')
            if is_prime(num):
                count+=1
        return count
