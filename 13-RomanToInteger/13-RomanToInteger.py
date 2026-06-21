# Last Updated: 6/22/2026, 12:45:27 AM
class Solution:
    def romanToInt(self, s: str) -> int:
        special = {
            "IV": 4, "IX": 9,
            "XL": 40, "XC": 90,
            "CD": 400, "CM": 900
        }

        normal = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100,
            "D": 500, "M": 1000
        }

        i = 0
        res = 0

        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in special:
                res += special[s[i:i+2]]
                i += 2
            else:
                res += normal[s[i]]
                i += 1

        return res