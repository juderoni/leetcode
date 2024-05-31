class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums2 = []
        for i in nums:
            if (i != val):
                nums2.append(i)
        k = 0
        for i, item in enumerate(nums2):
            k+=1
            nums[i] = item
        return k
