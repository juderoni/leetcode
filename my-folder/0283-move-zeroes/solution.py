class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # iterate through, see non zero, send to front,
        # keep index of where "front" is.
        # front is not really front, just where to put nextitem
        front = 0
        for i, item in enumerate(nums):
            if item == 0:
                continue
            else:
                nums[front] = item
                if front != i:

                    nums[i] = 0
                front+=1
        
