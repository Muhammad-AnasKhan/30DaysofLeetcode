class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        nums_set = set(nums)
        print(nums_len)
        for i in range(0, nums_len+1):
            if i not in nums_set:
                return i
        return -1