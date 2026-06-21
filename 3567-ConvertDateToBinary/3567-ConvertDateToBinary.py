# Last Updated: 6/21/2026, 7:02:17 PM
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        binary=""
        temp=""
        n=len(date)
        i=0
        while i<n:
            if date[i]=='-':
                binary+=str(bin(int(temp))[2:])+'-'
                temp=""
            else:
                temp+=date[i]
            i+=1
        binary+=str(bin(int(temp))[2:])
        return binary