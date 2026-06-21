# Last Updated: 6/21/2026, 7:06:24 PM
class Solution:
    def compress(self, chars: List[str]) -> int:
        char=chars[0]
        count=0
        res=[]
        index=0
        for c in chars:
            if char==c:
                count+=1
            else:
                res.append(char)
                if 1<count<=9:
                    res.append(str(count))
                elif count>9:
                    res.extend([x for x in str(count)])
                count=1
                char=c
        if count:
            res.append(char)
            if 1<count<=9:
                res.append(str(count))
            elif count>9:
                res.extend([x for x in str(count)])

        chars[::]=res
        return len(res)
