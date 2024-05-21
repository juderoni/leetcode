class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        threshold = maxCandies - extraCandies
        rtn = []
        for i in candies:
            if (i >= threshold):
                rtn.append(True)
            else:
                rtn.append(False)
        return rtn
