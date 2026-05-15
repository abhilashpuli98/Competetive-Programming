# Last Updated: 5/15/2026, 11:11:00 PM
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        e1,e2="",""
        o1,o2="",""
        for i in range(len(s1)):
            if i%2==0:
                e1+=s1[i]
                e2+=s2[i]
            else:
                o1+=s1[i]
                o2+=s2[i]
        e1=sorted(e1)
        e2=sorted(e2)
        o1=sorted(o1)
        o2=sorted(o2)
        return o1==o2 and e1==e2