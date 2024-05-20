class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        totlen = len(word1) + len(word2)
        fin = ""
        for i in range(totlen):
            if (i < len(word1)):
                fin += word1[i]
            if (i < len(word2)):
                fin+= word2[i]
            
        
        return fin

