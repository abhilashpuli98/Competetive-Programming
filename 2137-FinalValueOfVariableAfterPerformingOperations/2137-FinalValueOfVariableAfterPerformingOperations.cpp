// Last Updated: 5/15/2026, 11:12:01 PM
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int result = 0 ; 
        for ( string opr : operations) result+=(opr[1] == '+' ? 1 : -1);
        return result;
    }
};