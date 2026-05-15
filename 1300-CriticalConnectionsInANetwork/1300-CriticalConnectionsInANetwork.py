# Last Updated: 5/15/2026, 11:13:45 PM
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph=[[] for _ in range(n)]
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*n
        tin=[-1]*n
        low=[-1]*n
        timer=1
        bridges=[]
        def dfs(node,parent):
            visited[node]=True
            nonlocal timer
            tin[node]=low[node]= timer
            timer+=1
            for adj in graph[node]:
                if adj==parent:
                    continue
                if not visited[adj]:
                    dfs(adj,node)
                    #Update the low w.r.t min of adjnode low and node's low
                    low[node]=min(low[node],low[adj])
                    #now we have to check can this node---adj be bridge?=> we have to check
                    #low[adj]<=tin[node]---> we can reach back if its > then it's a bridge
                    if low[adj]>tin[node]:
                        bridges.append([adj,node])
                #if its already visted and we still comming back its still in same compo
                else:
                    low[node]=min(low[node],low[adj])
        dfs(0,-1)
        return bridges


