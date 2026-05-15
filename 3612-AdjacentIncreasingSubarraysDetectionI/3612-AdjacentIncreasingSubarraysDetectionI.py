# Last Updated: 5/15/2026, 11:10:16 PM
class Solution:
    def hasIncreasingSubarrays(self, a: List[int], k: int) -> bool:
        return any(all(all(starmap(lt,pairwise(a[j:j+k]))) for j in (i,i+k))
            for i in range(len(a)-2*k+1))