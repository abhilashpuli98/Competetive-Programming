# Last Updated: 6/22/2026, 12:44:14 AM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[]
        maxi=float('-inf')
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                curr_height=heights[stack.pop()]
                nse=i
                pse=stack[-1] if stack else -1
                width=nse-pse-1
                maxi=max(maxi,width*curr_height)
            stack.append(i)
        return maxi