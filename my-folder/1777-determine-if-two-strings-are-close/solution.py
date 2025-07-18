class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # rule one basically says order doesn't matter
        # rule two says the content of list of the frequency of characters 
        # is the same for each charcter
        # sets must be the same

        if set(word1) != set(word2) or len(word1) != len(word2):
            return False

        freqMap1 = self.getFreqMaps(word1)
        freqMap2 = self.getFreqMaps(word2)
        print(freqMap1)
        print(freqMap2)
        freqMapList1 = list(freqMap1.values())
        freqMapList2 = list(freqMap2.values())
        freqMapList1.sort()
        freqMapList2.sort()
        if freqMapList1 == freqMapList2:
            return True
        else:
            return False
        # size of this array can't be more than 26, which is size of alphabet



        return True
        
    def getFreqMaps(self, word):
        retFreqMap = {}
        for i in word:
            if i in retFreqMap:
                retFreqMap[i] += 1
            else:
                retFreqMap[i] = 1
        return retFreqMap
