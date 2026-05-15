# Last Updated: 5/15/2026, 11:12:00 PM
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct=[]
        count=0
        counter=Counter(arr)
        for item in arr:
            if counter[item]==1:
                count+=1
            if count==k:
                return item
        return ""