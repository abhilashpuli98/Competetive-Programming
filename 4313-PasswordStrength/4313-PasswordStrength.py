# Last Updated: 6/21/2026, 7:01:45 PM
class Solution:
    def passwordStrength(self, password: str) -> int:
        contribution=0
        for char in set(list(password)):
            if 'a'<=char<='z':
                contribution+=1
            if 'A'<=char<='Z':
                contribution+=2
            if '0'<=char<='9':
                contribution+=3
            if char in "!@#$":
                contribution+=5
        return contribution

