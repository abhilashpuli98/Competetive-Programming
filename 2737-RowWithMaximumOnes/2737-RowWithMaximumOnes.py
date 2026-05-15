# Last Updated: 5/15/2026, 11:11:12 PM
class Solution:
    def rowAndMaximumOnes(self, mat):
        index = 0
        max_count = 0
        for i, row in enumerate(mat):
            curr = sum(row)
            if curr > max_count:
                max_count = curr
                index = i

        return [index, max_count]