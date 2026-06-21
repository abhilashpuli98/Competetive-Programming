# Last Updated: 6/22/2026, 12:43:38 AM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        parts=[]
        def isPalindrome(left,right):
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def dfs(i):
            if i>=len(s):
                res.append(parts.copy())
                return
            for indx in range(i,len(s)):
                if isPalindrome(i,indx):
                    parts.append(s[i:indx+1])
                    dfs(indx+1)
                    parts.pop()
        dfs(0)
        return res