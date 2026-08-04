# Last Updated: 8/5/2026, 12:31:10 AM
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance=[[float('inf')]*n for _ in range(n)]
        for node in range(n):
            distance[node][node]=0
        for node1,node2,dist in edges:
            distance[node1][node2]=dist
            distance[node2][node1]=dist
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][via]!=float('inf') and distance[via][j]!=float('inf'):
                        distance[i][j]=min(distance[i][j],distance[i][via]+distance[via][j])
        mini=n
        res=-1
        for src in range(n):
            count=0
            for dst in range(n):
                if distance[src][dst]<=distanceThreshold:
                    count+=1
            if count<=mini:
                mini=count
                res=src
        return res