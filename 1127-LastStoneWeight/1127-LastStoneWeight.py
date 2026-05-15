# Last Updated: 5/15/2026, 11:14:04 PM
class Solution(object):
    def lastStoneWeight(self, stones):
        stones=[-i for i in stones];
        heapq.heapify(stones);
        while(len(stones)>1):
            y=-heapq.heappop(stones);
            x=-heapq.heappop(stones);
            heapq.heappush(stones,x-y);
        return -heapq.heappop(stones)
        """
        :type stones: List[int]
        :rtype: int
        """
        