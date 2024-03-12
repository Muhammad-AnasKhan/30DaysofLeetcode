/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
        // Initialize memory to all arrays 
        let left = []; 
        let right = []; 
        let product = []; 
   
        let i, j; 
   
        /* Left most element of left array is always 1 */
        left[0] = 1; 
   
        /* Right most element of right array is always 1 */
        right[nums.length - 1] = 1; 
   
        /* Construct the left array */
        for (i = 1; i < nums.length; i++) 
            left[i] = nums[i - 1] * left[i - 1]; 
   
        /* Construct the right array */
        for (j = nums.length - 2; j >= 0; j--) 
            right[j] = nums[j + 1] * right[j + 1]; 
   
        /* Construct the product array using left[] and right[] */
        for (i = 0; i < nums.length; i++) 
            product[i] = left[i] * right[i]; 
   
       
        return product; 
};