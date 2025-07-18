class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # iterate throught the list and see what numbers add with each other
        # ahh, subtract from k and look for abs ==
        # basically 
        # 1 2 3 4 k=5
        # -4 -3 -2 -1
        # we match 1 with -1 
        # we basically say, have we seen 4 in the opposite list
        count = 0
        mapTing = {}
        for i, item in enumerate(nums):
            res = k - item
            
            if res in mapTing:
                if mapTing[res] == 1:
                    mapTing.pop(res)
                else:
                    mapTing[res] -= 1
                count += 1
                
            else:
                if item in mapTing:
                    mapTing[item] += 1
                else:
                    mapTing[item] = 1
        print(mapTing)
        return count
        

        

