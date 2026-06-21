# Last Updated: 6/22/2026, 12:44:20 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        n=len(nums)
        freqDict={}
        k=0
        for num in (nums):
            freqDict[num]=freqDict.get(num,0)+1
            if freqDict[num]<=2:
                nums[k]=num
                k+=1
        return k
        