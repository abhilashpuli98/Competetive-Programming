# Last Updated: 6/21/2026, 7:03:45 PM
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq=Counter(digits)
        res=[]
        for x in range(100,1000,2):
            y0,y1,y2=x%10,(x//10)%10,x//100
            freq[y0]-=1
            freq[y1]-=1
            freq[y2]-=1
            if freq[y0]>=0 and freq[y1]>=0 and freq[y2]>=0:
                res.append(x)
            freq[y0]+=1
            freq[y1]+=1
            freq[y2]+=1
        return res
            