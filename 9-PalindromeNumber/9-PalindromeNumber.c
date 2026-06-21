// Last Updated: 6/22/2026, 12:45:36 AM
bool isPalindrome(int x)
{
long long sum=0,ld,on=x;
    while(x>0)
    {
        ld=x%10;
        sum=sum*10+ld;
        x=x/10;        
    }
    if (sum==on)
        return true;
    return false;
}
