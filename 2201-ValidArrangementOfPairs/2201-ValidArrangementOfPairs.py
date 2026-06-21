# Last Updated: 6/21/2026, 7:03:49 PM
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        inoutDeg=defaultdict(int)
        graph=defaultdict(list)
        path=[]
        for start,end in pairs:
            graph[start].append(end)
            inoutDeg[start]+=1
            inoutDeg[end]-=1
        start=pairs[0][0]
        for node in inoutDeg:
            if inoutDeg[node]==1:
                start=node
                break
        def dfs(node):
            while graph[node]:
                nei=graph[node].pop()
                dfs(nei)
                path.append([node,nei])
        dfs(start)
        return path[::-1]
