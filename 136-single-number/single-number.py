from functools import reduce
from operator import xor

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1-using reduce and xor methods
        return reduce(xor, nums) 

        # 2-using XOR operator to skip the duplicates
        # result = 0
        # for num in nums:
        #     result ^= num
        # return result


        