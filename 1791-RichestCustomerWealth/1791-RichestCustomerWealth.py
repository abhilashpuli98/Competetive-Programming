# Last Updated: 5/15/2026, 11:12:45 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in range(len(accounts)):
            maxi=max(maxi,sum(accounts[i]))
        return maxi
