# Last Updated: 5/15/2026, 11:12:29 PM
class Solution:
    def beautySum(self, s: str) -> int:
        def max_min():
            maxi=float('-inf')
            mini=float('inf')
            for i in range(26):
                if freq[i]>0:
                    maxi=max(maxi,freq[i])
                    mini=min(mini,freq[i])
            return maxi-mini if maxi!=float('-inf') and mini!=float('inf') else 0
        total=0
        for i in range(len(s)):
            freq=[0]*26
            for j in range(i,len(s)):
                freq[ord(s[j])-ord('a')]+=1
                total+=max_min()
        return total
