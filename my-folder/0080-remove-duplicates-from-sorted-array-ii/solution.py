class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i, item in enumerate(nums):
            if (k == 0 or k == 1 or nums[k - 2] != item):
                nums[k] = item
                k+=1
                


        return k
