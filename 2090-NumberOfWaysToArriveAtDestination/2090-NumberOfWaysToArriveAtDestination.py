# Last Updated: 5/15/2026, 11:12:06 PM
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9+7
        graph=[[] for _ in range(n)]
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        ways=[0]*n
        pq=[]
        visited=set()
        heapq.heappush(pq,(0,0))
        dist=[float('inf')]*(n)
        dist[0]=0
        ways[0]=1
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist[u]:
                continue
            for v,w in graph[u]:
                if dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
                    ways[v]=ways[u]
                    heapq.heappush(pq,(dist[v],v))
                elif dist[u]+w==dist[v]:
                    ways[v]=(ways[v]+ways[u])%MOD
        return ways[n-1]%MOD