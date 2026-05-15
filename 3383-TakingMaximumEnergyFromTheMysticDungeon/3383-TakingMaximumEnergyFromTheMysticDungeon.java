// Last Updated: 5/15/2026, 11:10:47 PM
class Solution {
    public int maximumEnergy(int[] energy, int k) {
        int maxEnergy=Integer.MIN_VALUE;
        int n=energy.length;
        int energySequence[] = new int[n];
        for (int x=n-1 ; x>=0 ; x--){
            energySequence[x] = energy[x]+(x+k<n? energySequence[x+k] : 0);
            maxEnergy = Math.max(maxEnergy,energySequence[x]);
        }
        return maxEnergy;
    }
}