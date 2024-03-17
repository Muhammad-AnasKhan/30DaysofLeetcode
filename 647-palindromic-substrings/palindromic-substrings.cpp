class Solution {
public:
    int countSubstrings(std::string s) {
        int count = 0;
        int n = s.length();

        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                std::string substr = s.substr(i, j - i + 1);
                if (isPalindrome(substr)) {
                    count++;
                }
            }
        }

        return count;
    }

private:
    bool isPalindrome(std::string str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str[left] != str[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};