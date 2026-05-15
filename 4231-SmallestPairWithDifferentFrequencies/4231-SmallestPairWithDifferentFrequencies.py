# Last Updated: 5/15/2026, 11:09:14 PM
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counter=Counter(nums)
        values=sorted(counter.keys())
        for i in range(len(values)):
            for j in range(i+1,len(values)):
                if counter[values[i]]!=counter[values[j]]:
                    return [values[i],values[j]]
        return [-1,-1]