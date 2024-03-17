class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numlist = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j < i:
                    if(nums[i]+nums[j]==target):
                        numlist.extend([i, j])
                        return numlist
                
           
        
        