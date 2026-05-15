# Last Updated: 5/15/2026, 11:09:12 PM
class Solution:
    def reverseByType(self, s: str) -> str:
        left,right=0,len(s)-1
        letters=[]
        spls=[]
        for ch in s:
            if 'a'<=ch<='z':
                letters.append(ch)
            else:
                spls.append(ch)
        letters.reverse()
        spls.reverse()
        res=[]
        l=sp=0
        for ch in s:
            if 'a'<=ch<='z':
                res.append(letters[l])
                l+=1
            else:
                res.append(spls[sp])
                sp+=1
        return "".join(res)