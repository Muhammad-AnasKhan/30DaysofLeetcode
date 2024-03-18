class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using set

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # without using set

        # nums.sort()  # Sort the array
        # n = len(nums)
        # for i in range(n - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False

        # clever technique - one liner
        return len(set(nums))!=len(nums)