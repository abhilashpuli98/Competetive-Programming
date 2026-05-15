# Last Updated: 5/15/2026, 11:10:54 PM
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxEnergy = float('-inf')
        energySequence = [0]*len(energy)
        for x in range(len(energy)-1,-1,-1):
            energySequence[x] = energy[x]+(energySequence[x+k] if x+k<len(energy) else 0)
            maxEnergy = max(maxEnergy,energySequence[x])
        return maxEnergy
