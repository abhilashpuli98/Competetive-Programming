# Last Updated: 5/15/2026, 11:10:20 PM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq=[0]*len(nums)
        res=[]
        for num in nums:
            if freq[num]==1:
                res.append(num)
            else:
                freq[num]+=1
        return res 
