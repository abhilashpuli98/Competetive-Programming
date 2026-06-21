# Last Updated: 6/21/2026, 7:06:41 PM
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn>8:
            return []
        result=[]
        for hr in range(12):
            for mins in range(60):
                if hr.bit_count()+mins.bit_count()==turnedOn:
                    result.append(f'{hr}:{mins:02d}')
        return result