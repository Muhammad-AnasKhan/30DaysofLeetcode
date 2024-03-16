class Solution:
    def findMin(self, nums: List[int]) -> int:
        # using min()
        # return min(nums)


        # without min() 
        min_integer = nums[0]  # suppose
        for num in nums:
            if num < min_integer:
                min_integer = num  # Update if  found

        return min_integer
        