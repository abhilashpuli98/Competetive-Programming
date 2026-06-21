# Last Updated: 6/22/2026, 12:45:39 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxi=0
        result=""
        for i in range(n):
            r=l=i
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>maxi:
                    maxi=max(maxi,r-l+1)
                    result=s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>maxi:
                    maxi=max(maxi,r-l+1)
                    result=s[l:r+1]
                l-=1
                r+=1
        return result
