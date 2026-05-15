# Last Updated: 5/15/2026, 11:11:27 PM
class Solution:
    def longestCycle(self, edges):
        ans=-1
        def dfs(node,dist,visited):
            visited[node]=True
            path[node]=True
            nei=edges[node]
            if nei!=-1 and not visited[nei]:
                dist[nei]=dist[node]+1
                dfs(nei,dist,visited)
            elif nei!=-1 and path[nei]:
                nonlocal ans
                ans=max(ans,dist[node]-dist[nei]+1)
            path[node]=False
        visited=[False]*(len(edges))
        dist=[-1]*(len(edges))
        path=[False]*(len(edges))
        for i in range(len(edges)):
            if not visited[i]:
                dist[i]=0
                dfs(i,dist,visited)
        return ans