class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1
        p1 = m - 1  # Pointer for the end of the non-empty part of nums1
        p2 = n - 1  # Pointer for the end of nums2
        p = m + n - 1  # Pointer for the end of nums1 (where we'll merge backwards)

        # Merge from the largest elements
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]: 
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        nums1[:p2 + 1] = nums2[:p2 + 1]  

            