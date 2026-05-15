# Last Updated: 5/15/2026, 11:14:31 PM
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q=deque([x for x in range(len(deck))])
        ans=[0]*len(q)
        for i in range(len(deck)):
            index=q.popleft()
            ans[index]=deck[i]
            if q:
                q.append(q.popleft())
        return ans

