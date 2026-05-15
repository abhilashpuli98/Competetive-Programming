# Last Updated: 5/15/2026, 11:11:46 PM
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        count=[0]*10001
        for i in range(len(growTime)):
            count[growTime[i]]+=plantTime[i]#Replaces the plant time at growTime[i] If multiple plants have the same grow time, only the last one survives
        possible=0
        curr=0
        for i in range(10000,0,-1):
            if count[i]!=0:
                curr+=count[i]
                possible=max(possible,curr+i)
        return possible

