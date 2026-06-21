# Last Updated: 6/22/2026, 12:42:35 AM
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        isPrime=[True]*(n)

        isPrime[0]=isPrime[1]=False
        for i in range(2,int(n**0.5)+1):
            if isPrime:
                for x in range(i*i,n,i):
                    isPrime[x]=False
        return sum(isPrime)