# Last Updated: 6/21/2026, 7:03:35 PM
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n=len(people)
        start=[]
        end=[]
        for i,j in flowers:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        return [bisect_right(start,people[i])-bisect_left(end,people[i]) for i in range(n) ]
        