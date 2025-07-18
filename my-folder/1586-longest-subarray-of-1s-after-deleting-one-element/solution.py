class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # two groups can be compared at a time
        left = 0
        maxCount = 0
        lastIndex0 = -1

        for right in range(len(nums)):
            if nums[right] == 0:
                left = lastIndex0 + 1
                lastIndex0 = right
            maxCount = max(maxCount, right - left)
        return maxCount
        
                
