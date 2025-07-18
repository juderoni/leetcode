class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altList = [0]
        summer = 0
        for i in range(len(gain)):
            summer += gain[i]
            altList.append(summer)
        
        return max(altList)
