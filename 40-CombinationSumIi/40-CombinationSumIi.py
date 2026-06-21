# Last Updated: 6/22/2026, 12:44:57 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos=[]
        res=[]
        candidates.sort()
        def backtracker(i,csum):
            if csum>target:
                return
            if csum==target:
                res.append(combos[:])
                return
            for start in range(i,len(candidates)):
                if start!=i and candidates[start]==candidates[start-1]:
                    continue
                combos.append(candidates[start])
                backtracker(start+1,csum+candidates[start])
                combos.pop()
        backtracker(0,0)
        return res