# Last Updated: 6/21/2026, 7:06:51 PM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=Counter(nums1)
        result=[]
        for i in range(len(nums2)):
            if nums1[nums2[i]]>0:
                result.append(nums2[i])
                nums1[nums2[i]]-=1  #Dont forget to return count else multiple same values may append
        return result