class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        # 1 2 3 4
        # 1 1 2 6

        # 1  2  3  4
        # 24 12 4. 1
        # two lists mult together
        outputList = [1]
        curr = 1
        for i in range(1, len(nums)):
            curr = curr * nums[i - 1]
            outputList.append(curr)
        
        print(outputList)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            outputList[i] *= curr
            curr *= nums[i]
        return outputList
        
        
