class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        # for each number we want to store that number and the number before it.
        longest = 1
        if len(nums) == 0:
            return 0

        # basically we want to go through nums, and query 
        #
        for i in setnum:
            # query the "first" of a series of numbers
            if i - 1 not in setnum:
                # ask if i has values that are +1 larger later in the list
                localLongest = 1
                while i + localLongest in setnum:
                    localLongest += 1
                longest = max(localLongest, longest)

        return longest
                    

        
        
            
            

