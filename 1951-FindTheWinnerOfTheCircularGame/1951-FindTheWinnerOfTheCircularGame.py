# Last Updated: 5/15/2026, 11:12:26 PM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count=1
        q=deque()
        for i in range(1,n+1):
            q.append(i)
        while len(q)>1:
            for i in range(1,k):
                q.append(q.popleft())
            q.popleft()
        return q[-1]