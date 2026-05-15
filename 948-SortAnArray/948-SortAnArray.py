# Last Updated: 5/15/2026, 11:14:41 PM
class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        self.mergeSort(arr,0,len(arr))
        return arr
    def mergeSort(self, arr, l, r):
        if l<r:
            mid=(l+r)//2
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr,l,mid,r)
    def merge(self,arr,l,mid,h):
        L=arr[l:mid+1]
        R=arr[mid+1:h+1]
        left=0
        right=0
        k=l
        while left<len(L) and right<len(R):
            if L[left]<=R[right]:
                arr[k]=L[left]
                left+=1
            else:
                arr[k]=R[right]
                right+=1
            k+=1
        if left<len(L):
            arr[k:k+len(L)-left]=L[left:]
        if right<len(R):
            arr[k:k+len(R)-right]=R[right:]
            
            
            
            