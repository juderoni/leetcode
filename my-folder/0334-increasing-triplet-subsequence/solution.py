class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # only asking for if there are 3 numbers that at increasing at any point
        # so just go through and see if numbers show up that are bigger than the min
        # track smallest and second smallest nums seen so far

        largest = max(nums)
        firstSmallest = largest
        secondSmallest = largest

        for i in range(len(nums)):
            if firstSmallest >= nums[i]:
                firstSmallest = nums[i]
            elif secondSmallest >= nums[i]:
                secondSmallest = nums[i]
            else:
                return True
        return False
