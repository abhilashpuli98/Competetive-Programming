# Last Updated: 7/9/2026, 12:18:06 AM
class Solution:
        def countPrefixSuffixPairs(self, words: List[str]) -> int:
            count=0
            for i in range(len(words)):
                for j in range(i+1,len(words)):
                    if len(words[i])>len(words[j]):
                        continue
                    if words[j][:len(words[i])]==words[i] and words[j][len(words[j])-len(words[i]):]==words[i]:
                        count+=1
            return count