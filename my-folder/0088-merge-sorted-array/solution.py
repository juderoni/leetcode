class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in reversed(range(m+n)):
            
            if m - 1 < 0:
                nums1[i] = nums2[n - 1]
                n-=1
            elif n - 1 < 0:
                nums1[i] = nums1[m - 1]
                m-=1
            elif (nums1[m - 1] >= nums2[n - 1]):
                nums1[i] = nums1[m - 1]
                m-=1
            elif (nums1[m - 1] < nums2[n - 1]):
                nums1[i] = nums2[n - 1]
                n-=1
        


            

        
