# Last Updated: 5/15/2026, 11:14:59 PM
class Solution: 
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited=[0]*len(graph)
        safe=[0]*len(graph)
        res=[]
        pathv=[0]*len(graph)
        def dfs(node):
            
            visited[node]=1
            pathv[node]=1
            for adj in graph[node]:
                if not visited[adj]:
                    if dfs(adj):
                        return True
                elif pathv[adj]:
                    return True
            pathv[node]=0
            safe[node]=1
            res.append(node)
            return False
        for i in range(len(graph)):
            if not visited[i]:
                dfs(i)
                    
        return sorted(res)
                    

