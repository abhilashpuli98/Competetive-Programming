# Last Updated: 5/15/2026, 11:12:17 PM
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph=[[] for _ in range(len(passingFees))]
        for u,v,time in edges:
            graph[u].append((time,v))
            graph[v].append((time,u))
        pq=[(passingFees[0],0,0)]
        dist=[[float('inf')]*(maxTime+1) for _ in range(len(passingFees))]
        while pq:
            cost,time,node=heapq.heappop(pq)
            if node==len(passingFees)-1:
                return cost
            for curr_time,adj in graph[node]:
                new_time=curr_time+time
                if new_time>maxTime or cost>dist[node][time]:
                    continue
                if passingFees[adj]+cost<dist[adj][new_time]:
                    dist[adj][new_time]=passingFees[adj]+cost
                    heapq.heappush(pq,(passingFees[adj]+cost,new_time,adj))
        return -1
