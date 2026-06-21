# Last Updated: 6/21/2026, 7:06:05 PM
class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[-1]*n
        stack=[]
        for i in range(2*n-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i%n]:
                stack.pop()
            if stack:
                res[i%n]=arr[stack[-1]]
            stack.append(i%n)
        return res