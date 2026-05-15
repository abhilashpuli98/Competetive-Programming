# Last Updated: 5/15/2026, 11:14:55 PM
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q=deque(([0]))
        visited=set([0])
        #visited.add(0)
        while q:
            key=q.popleft()
            for room in rooms[key]:
                if room not in visited:
                    q.append(room)
                    visited.add(room)
        return len(visited)==len(rooms)
