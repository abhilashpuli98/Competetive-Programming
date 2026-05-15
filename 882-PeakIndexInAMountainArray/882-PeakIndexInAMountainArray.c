// Last Updated: 5/15/2026, 11:14:52 PM
int peakIndexInMountainArray(int* arr, int n) {
    int low=0;
    int high=n-1;
    int mid;
    while(low<=high)
    {
        mid=low+(high-low)/2;
        if(arr[mid]<arr[mid+1])
        low=mid+1;
        else
        high=mid-1;
    }
    return low;
    
}