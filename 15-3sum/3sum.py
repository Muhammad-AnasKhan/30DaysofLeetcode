class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        nums_len = len(nums)
        triplets = []

        # approach used
        '''
            fixing the one value
            and finding sum of any other(two sum) to 
            find the opposite of the above fixed value.

            n1 + n2 + n3 == 0
        '''
        
        for i in range(nums_len-2): # prevents unnecessary iterations
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates 

            left = i + 1
            right = nums_len -1

            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates if exists
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets


        