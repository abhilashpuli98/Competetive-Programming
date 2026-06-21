# Last Updated: 6/22/2026, 12:42:29 AM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        def topology_sort():
            res=[]
            in_degree=[0]*numCourses
            for i in range(numCourses):
                for node in adj[i]:
                    in_degree[node]+=1
            q = deque()
            for i in range(numCourses):
                if in_degree[i]==0:
                    q.append(i)
            while q:
                node=q.popleft()
                res.append(node)
                for cn in adj[node]:
                    in_degree[cn]-=1
                    if in_degree[cn]==0:
                        q.append(cn)
            return res if len(res)==len(adj) else []
        return topology_sort()
                    
        
        