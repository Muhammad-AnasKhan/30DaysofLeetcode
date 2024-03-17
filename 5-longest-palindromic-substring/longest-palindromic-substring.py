class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        n = len(s)
        max = 1
        max_substr = s[0]
        for i in range(n):
            for j in range(i, n):
                substr = s[i:j+1]
                # print(substr)
                if substr == substr[::-1]:
                    # print(substr)
                    if len(substr) > max: 
                        max = len(substr)
                        max_substr = substr

        return max_substr
        