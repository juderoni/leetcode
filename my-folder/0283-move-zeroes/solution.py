class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numtimespopped = 0
        for i in range(len(nums)):
            reali = i - numtimespopped
            if (nums[reali] == 0):
                nums.pop(reali)
                nums.append(0)
                numtimespopped += 1
        
        
