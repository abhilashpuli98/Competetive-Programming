# Last Updated: 5/15/2026, 11:12:08 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        resultant=0
        for opr in operations:
            if opr in ["++X","X++"]:
                resultant+=1
            else:
                resultant-=1
        return resultant