class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numlist = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j < i:
        #             if(nums[i]+nums[j]==target):
        #                 numlist.extend([i, j])
        #                 return numlist
        
        
        #2 Create a dictionary to store the complement of each number
        complement_dict = {}

        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            # print(complement_dict)
            # Check if the complement exists in the dictionary
            if complement in complement_dict:
                # If found, return the indices of the two numbers
                return [complement_dict[complement], i]
            
            # Otherwise, store the current number and its index in the dictionary
            complement_dict[num] = i
        
        # If no solution is found, return None
        return None
                
           
        
        