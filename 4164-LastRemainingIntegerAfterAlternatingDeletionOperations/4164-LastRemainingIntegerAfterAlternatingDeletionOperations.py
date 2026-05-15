# Last Updated: 5/15/2026, 11:09:20 PM
class Solution(object):
    def lastInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        toravianel = n

        head = 1
        step = 1
        remaining = n
        left = True

        while remaining > 1:
            if not left and remaining % 2 == 0:
                head += step
            remaining = (remaining + 1) // 2
            step *= 2
            left = not left

        return head