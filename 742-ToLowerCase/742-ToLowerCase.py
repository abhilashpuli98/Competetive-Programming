# Last Updated: 5/15/2026, 11:15:18 PM
class Solution:
    def toLowerCase(self, s: str) -> str:
        result=""
        for letter in s:
            if 'A'<=letter<='Z':
                result+=chr(ord(letter)+32)
            else:
                result+=letter
        return result
        