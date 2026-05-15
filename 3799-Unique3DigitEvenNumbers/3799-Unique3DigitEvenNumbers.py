# Last Updated: 5/15/2026, 11:09:50 PM
class Solution:
    def totalNumbers(self, nums: List[int]) -> int:
        freq=Counter(nums)
        count=0
        for i in range(100,1000):
            h=i//100
            t=(i//10)%10
            u=(i)%10
            if u%2!=0:
                continue
            need=Counter([h,t,u])
            if all(freq[d]>=need[d] for d in need):
                count+=1
        return count