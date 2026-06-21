// Last Updated: 6/21/2026, 7:06:48 PM
bool isPerfectSquare(int n) {
    long mid,low=0,high=n-1;
    while(low<=high)
    {
        mid=low+(high-low)/2;
        if(n==0||n==1)
        return true;
        if(mid*mid==n)
        return true;
        else if(mid*mid<n)
        low=mid+1;
        else
        high=mid-1;

    }
    return false;

    
}