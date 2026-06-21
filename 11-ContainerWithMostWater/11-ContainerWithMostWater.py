# Last Updated: 6/22/2026, 12:45:28 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=float('-inf')
        left,right=0,len(height)-1
        while left<right:
            area=max(area,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area