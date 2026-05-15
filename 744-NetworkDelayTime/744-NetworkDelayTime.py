# Last Updated: 5/15/2026, 11:15:16 PM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        pq = []
        dist=[float('inf')] * (n+1)
        dist[k]=0
        heapq.heappush(pq,(0, k))
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist[u]:
                continue
            for v,w in graph[u]:
                if dist[u]+w< dist[v]:
                    dist[v]=dist[u] + w
                    heapq.heappush(pq,(dist[v], v))
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1