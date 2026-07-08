# Last Updated: 7/9/2026, 12:17:29 AM
class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        from functools import lru_cache
        MOD=10**9+7
        @lru_cache(None)
        def dfs(i,p1,p2,m):
            if i==len(target):
                return m==3
            ans=0
            for j in range(p1,len(word1)):
                if word1[j]==target[i]:
                    ans+=dfs(i+1,j+1,p2,m|1)
            for j in range(p2,len(word2)):
                if word2[j]==target[i]:
                    ans+=dfs(i+1,p1,j+1,m|2)
            return ans%MOD
        return dfs(0,0,0,0)
            