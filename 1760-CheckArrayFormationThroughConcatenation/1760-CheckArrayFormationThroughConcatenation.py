# Last Updated: 5/15/2026, 11:12:47 PM
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp={sm[0]:sm for sm in pieces}
        new=[]
        for i in range(len(arr)):
            new+=mp.get(arr[i],[])
        return new==arr