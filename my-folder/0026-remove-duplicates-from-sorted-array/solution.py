class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        prevNumber = nums[0]
        if len(nums) == 1:
            return 1
        
        for i in range(1, len(nums)):
            if (prevNumber != nums[i]):
                counter+=1
                nums[counter] = nums[i]
                prevNumber = nums[i]
        
        return counter + 1

