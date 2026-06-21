# Last Updated: 6/22/2026, 12:41:51 AM
class Solution:
    def nthUglyNumber(self, n: int):
        
        ugly=[1]*n
        i2=i3=i5=0
        for i in range(1,n):
            u2=ugly[i2]*2
            u3=ugly[i3]*3
            u5=ugly[i5]*5

            ugly[i]=nextEle=min(u2,u3,u5)
            if u2==nextEle:
                i2+=1
            if u3==nextEle:
                i3+=1
            if u5==nextEle:
                i5+=1
        return ugly[-1]
