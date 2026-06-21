# Last Updated: 6/21/2026, 7:06:40 PM
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        n=len(num)
        for i in range(n):
            while stack and stack[-1]>num[i] and k:
                stack.pop()
                k-=1
            stack.append(num[i])
        while k>0:
            stack.pop()
            k-=1
        x="".join(stack).lstrip('0')
        return x if x!='' else '0'
