# Last Updated: 5/15/2026, 11:14:33 PM
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(strs[0])):
            letters=[]
            for j in range(len(strs)):
                letters.append(strs[j][i])
            if letters != sorted(letters):
                count+=1
        return count
        