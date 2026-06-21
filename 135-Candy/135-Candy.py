# Last Updated: 6/22/2026, 12:43:35 AM
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        up=0
        down=0
        peak=0
        s=1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                up+=1
                down=0
                peak=up
                s+=up+1
            elif ratings[i]==ratings[i-1]:
                up=0
                down=0
                peak=0
                s+=1
            else:
                down+=1
                up=0
                s+=down+1
                if down<=peak:
                    s=s-1

        return s
            