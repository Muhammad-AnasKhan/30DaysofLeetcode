class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                substr = s[i:j+1]
                if substr == substr[::-1]: # checking string with the reverse
                    count += 1

        return count
        