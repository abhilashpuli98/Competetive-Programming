# Last Updated: 5/15/2026, 11:11:26 PM
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            if num%2==0:
                freq[num] = freq.get(num,0)+1
        if not freq:
            return -1
        maxfreq=max(freq.values())
        return min(x for x in freq if freq[x]==maxfreq)