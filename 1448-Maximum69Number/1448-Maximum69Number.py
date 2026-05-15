# Last Updated: 5/15/2026, 11:13:29 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        result=""
        for i in range(len(num)):
            if num[i]=="6":
                result+="9"+num[i+1:]
                return int(result)
            else:
                result+=num[i]
        return int(num)