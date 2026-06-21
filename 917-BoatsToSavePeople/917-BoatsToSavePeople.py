# Last Updated: 6/21/2026, 7:05:04 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        mini=0
        people.sort()
        i,j=0,len(people)-1
        while i<=j:
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
            mini+=1
        return mini