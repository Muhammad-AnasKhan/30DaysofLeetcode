class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = current_min = max_so_far = nums[0]

        for num in nums[1:]:  
            temp_max = max(num, current_max * num, current_min * num)
            current_min = min(num, current_max * num, current_min * num)
            max_so_far = max(max_so_far, temp_max)
            current_max = temp_max

        return max_so_far
        