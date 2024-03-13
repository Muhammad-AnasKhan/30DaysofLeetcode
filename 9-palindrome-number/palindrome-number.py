class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse = ''
        for i in x:
            reverse = i + reverse # add each char to the beginning 
        if reverse == x:
            return True
        else:
            return False 
        