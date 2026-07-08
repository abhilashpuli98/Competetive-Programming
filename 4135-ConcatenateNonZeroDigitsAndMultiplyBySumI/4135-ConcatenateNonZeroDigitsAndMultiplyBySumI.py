# Last Updated: 7/9/2026, 12:17:27 AM
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        n=str(n)
        sum=0
        x=''
        for i in range(len(n)):
            if n[i]!='0':
                sum+=int(n[i])
                x+=n[i]
        return int(x)*sum
