class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string curr;
        backtrack(ans, curr, n, 0);
        return ans;
    }
    void backtrack(vector<string>& ans, string& curr, int left, int right) {
        if(left == 0 && right == 0) {
            ans.push_back(curr);
            return;
        }
        if(left > 0) {
            curr.push_back('(');
            backtrack(ans, curr, left - 1, right + 1);
            curr.pop_back();
        }
        if(right > 0) {
            curr.push_back(')');
            backtrack(ans, curr, left, right - 1);
            curr.pop_back();
        }
        
    }
};