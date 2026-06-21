# Last Updated: 6/22/2026, 12:42:34 AM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st={}
        ts={}
        for x,y in zip(s,t):
            if (x in st and st[x]!=y) or (y in ts and ts[y]!=x):
                return False
            st[x]=y
            ts[y]=x
        return True

        #return len(set(zip(s,t))) == len(set(s)) ==len(set(t))
