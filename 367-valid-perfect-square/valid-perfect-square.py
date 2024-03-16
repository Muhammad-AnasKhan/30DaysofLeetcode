class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # brute force

        # i = 1
        # # iterate untill reach to the perfect square(i * i) of 'num'
        # while i * i <= num:
        #     if i * i == num:
        #         return True
        #     i = i + 1
        # return False


        # Binary search

        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False

            
        