class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two numbers that add up the target are in the list.
        # each input one solution.
        # no same element twice.
        # [1,3,4,5] target = 6 rtn = [0, 3]
        # sub list = [5, 2, 2, 1]
        # probably going to make a second list that holds the subtraction of nums and target
        pairDict = {}
        
        for i, item in enumerate(nums):
            if target - item in pairDict:
                return [pairDict[target-item], i]
            pairDict[item] = i
        
        return [-1, -1]
        

        


        
        
