class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ting = {}
        if len(nums) == 1 or len(nums) == 2:
            return nums[0]
        for i in nums:
            if i in ting:
                ting[i] += 1
                if ting[i] >= len(nums)/2:
                    return i
            else:
                ting[i] = 1
        return 0 # doesn't work
        


