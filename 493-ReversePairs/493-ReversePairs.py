# Last Updated: 6/21/2026, 7:06:09 PM
class Solution:
    def __init__(self):
        self.count = 0

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    def countPairs(self,arr,low,mid,high):
        right=mid+1
        for i in range(low,mid+1):
            while right<=high and arr[i]>2*arr[right]:
                right+=1
            self.count+=(right-(mid+1))
    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.countPairs(arr,l,m,r)
            self.merge(arr, l, m, r)
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums, 0, len(nums) - 1)    
        return self.count