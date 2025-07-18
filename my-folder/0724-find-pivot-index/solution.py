class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # i think of making two lists
        # left sum and right sum list
        # maybe just left sum list and dreive right by subtraction
        # don't even need list

        sumTotal = sum(nums)
        leftTotal = 0

        for i in range(len(nums)):
            rightTotal = sumTotal - leftTotal - nums[i]

            if leftTotal == rightTotal:
                return i
            
            leftTotal = leftTotal + nums[i]
        return -1
