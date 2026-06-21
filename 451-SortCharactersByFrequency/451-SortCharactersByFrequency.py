# Last Updated: 6/21/2026, 7:06:21 PM
class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        buckets = [[] for i in range(len(s)+1)]
        for k,v in counter.items():
            buckets[v].append(k)
        res=""
        for i in range(len(buckets)-1,0,-1):
            for char in buckets[i]:
                res+=char*i
        return res
