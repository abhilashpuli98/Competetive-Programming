# Last Updated: 6/22/2026, 12:42:10 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1=None
        candidate2=None
        n=len(nums)
        res=[]
        vote1,vote2=0,0
        for num in nums:
            if candidate1==num:
                vote1+=1
            elif candidate2==num:
                vote2+=1
            elif vote1==0:
                candidate1=num
                vote1=1
            elif vote2==0:
                 candidate2=num
                 vote2=1
            else:
                vote1-=1
                vote2-=1
        threshold=n//3
        if nums.count(candidate1)>threshold:
            res.append(candidate1)
        if nums.count(candidate2)>threshold:
            res.append(candidate2)
        return res