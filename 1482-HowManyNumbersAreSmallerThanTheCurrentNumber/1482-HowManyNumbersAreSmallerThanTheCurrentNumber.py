# Last Updated: 5/15/2026, 11:13:18 PM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sml=[]
        count=0
        for i in  nums:
            for j in nums:
                if j<i:
                    count=count+1
            sml.append(count)
            count=0
        return sml