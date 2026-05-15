# Last Updated: 5/15/2026, 11:10:04 PM
class Solution:
    def findValidPair(self, s: str) -> str:
        s = list(s)
        freq = Counter(s)
        for i in range(1,len(s)):
            if s[i-1]!=s[i] and int(s[i]) == freq[s[i]] and int(s[i-1])==freq[s[i-1]]:
                return s[i-1]+s[i]
        return ""