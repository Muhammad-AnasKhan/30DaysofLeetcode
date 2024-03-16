class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        # iterate untill reach to the perfect square(i * i) of 'num'
        while i * i <= num:
            if i * i == num:
                return True
            i = i + 1
        return False

            
        