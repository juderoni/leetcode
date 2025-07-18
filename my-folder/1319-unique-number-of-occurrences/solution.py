class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqMap = {}
        for i in arr:
            if i in freqMap:
                freqMap[i] += 1
            else:
                freqMap[i] = 1
        
        # check fi the frequency is unique
        isUniqueSet = set()
        for i in set(arr):
            lenUSet = len(isUniqueSet)
            isUniqueSet.add(freqMap[i])
            if lenUSet+1 != len(isUniqueSet):
                return False
        
        return True
