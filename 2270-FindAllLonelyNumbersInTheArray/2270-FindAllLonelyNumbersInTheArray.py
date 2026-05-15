# Last Updated: 5/15/2026, 11:11:44 PM
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res=[]
        hm={}
        for num in nums:
            hm[num]=hm.get(num,0)+1
        for num in nums:
            if hm[num]==1 and  not hm.get(num+1,False) and not hm.get(num-1,False):
                res.append(num)
        return res