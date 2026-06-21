# Last Updated: 6/22/2026, 12:45:33 AM
class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        def skipSpaces():
            i=0
            while i<n and s[i]==" ":
                i+=1
            return i
        def parseInt(i,num):
            if i>=n or not('0'<=s[i]<='9'):
                return num
            num=num*10+(ord(s[i])-ord('0'))
            if num>2**31-1 or num < -2**31:
                return num
            return parseInt(i+1,num)
        indx=skipSpaces()
        sign=1
        if indx<n and (s[indx] in ['+','-']):
            sign= -1 if s[indx]=='-' else 1
            indx+=1
        parsed=parseInt(indx,0)
        if sign*parsed>2**31-1:
            return 2**31-1
        if sign*parsed < -2**31:
                return -2**31
        return parsed*sign
        