# Last Updated: 5/15/2026, 11:13:25 PM
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bitMap=collections.defaultdict(list)
        result=[]
        for num in arr:
            bitC=num.bit_count()
            bitMap[bitC].append(num)
        for key in sorted(bitMap.keys()):
            result.extend(sorted(bitMap[key]))
        return result
            
        