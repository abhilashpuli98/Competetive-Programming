# Last Updated: 5/15/2026, 11:15:07 PM
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        for i in range(len(arr)):
            if arr[i]==target:
                return i
            if arr[i]>target:
                return -1
        return -1