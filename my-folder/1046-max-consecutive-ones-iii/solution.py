class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # left right pointer
        # move right if k zeros have not been seen yet.
        # save largest distance between left and right (number of 1's)
        # move left if too many zeros are in the window.
        # keep track of how many zeros are within the window.

        left = 0
        right = 0
        numZeros = 0
        numOnes = 0
        longestConsecutive = 0
        while right != len(nums):
            if numZeros > k:
                if nums[left] == 0:
                    numZeros -= 1
                else:
                    numOnes -= 1
                left += 1
            else:
                
                if right == len(nums):
                    break
                if nums[right] == 1:
                    numOnes += 1
                else:
                    numZeros+=1
                right+=1
            
            if numZeros <= k:
                longestConsecutive = max(numOnes + numZeros, longestConsecutive)
        return longestConsecutive

        
        

