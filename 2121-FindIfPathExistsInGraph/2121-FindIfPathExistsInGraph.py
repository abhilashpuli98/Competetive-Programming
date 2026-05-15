# Last Updated: 5/15/2026, 11:12:03 PM
from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        g = {}
        for a, b in edges:
            if a not in g:
                g[a] = []
            if b not in g:
                g[b] = []
            g[a].append(b)
            g[b].append(a)
        q = deque([source])
        visit = set()
        visit.add(source)
        while q:
            x = q.popleft()
            if x == destination:
                return True
            for i in g[x]:
                if i not in visit:
                    visit.add(i)
                    q.append(i)
        return False