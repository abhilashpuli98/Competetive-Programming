# Last Updated: 6/21/2026, 7:03:47 PM
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj=defaultdict(list)
        for bi in range(len(bombs)):
            x1,y1,r1=bombs[bi]
            for bj in range(len(bombs)):
                if bi==bj:
                    continue
                x2,y2,r2=bombs[bj]
                distance=(x2-x1)**2+(y2-y1)**2
                if distance<=r1**2:
                    adj[bi].append(bj)
        def dfs(i):
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)
        res=0
        for i in range(len(bombs)):
            visited=set()
            dfs(i)
            res=max(res,len(visited))
        return res


