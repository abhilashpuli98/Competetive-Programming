# Last Updated: 5/15/2026, 11:11:58 PM
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens=s.split()
        prevNum=-1
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                currentNumber=int(tokens[i])
                if prevNum>=currentNumber:
                    return False
                else:
                    prevNum=currentNumber
        return True

        