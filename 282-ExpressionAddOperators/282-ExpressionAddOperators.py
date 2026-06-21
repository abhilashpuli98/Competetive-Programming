# Last Updated: 6/22/2026, 12:41:46 AM
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=[]
        def backtracker(i,curr_str,curr_sum,prev_num):
            if i>=len(num):
                if curr_sum==target:
                    res.append(curr_str)
                return
            for indx in range(i,len(num)):
                num_str=num[i:indx+1]
                n=int(num[i:indx+1])
                if not curr_str:
                    backtracker(indx+1,num_str,n,n)
                else:
                    backtracker(indx+1,curr_str+"+"+num_str,curr_sum+n,n)
                    backtracker(indx+1,curr_str+"-"+num_str,curr_sum-n,-n)
                    backtracker(indx+1,curr_str+"*"+num_str,curr_sum-prev_num+(prev_num*n),prev_num*n)
                if num[i]=='0':
                    break
        backtracker(0,"",0,0)
        return res
                    
