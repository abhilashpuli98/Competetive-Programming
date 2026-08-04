# Last Updated: 8/5/2026, 12:31:20 AM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mapper=Counter(text)
        return min(mapper.get('b', 0),
                mapper.get('a', 0),
                mapper.get('l', 0) // 2,
                mapper.get('o', 0) // 2,
                mapper.get('n', 0))