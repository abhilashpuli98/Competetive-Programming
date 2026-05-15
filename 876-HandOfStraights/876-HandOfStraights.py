# Last Updated: 5/15/2026, 11:14:53 PM
class Solution:
    def isNStraightHand(self, hand, W):
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(W)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True        