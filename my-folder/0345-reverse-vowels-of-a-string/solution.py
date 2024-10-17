class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        slist = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        while i < j and i != j:
            if slist[i] not in vowels:
                i+=1
            if slist[j] not in vowels:
                j-=1
            if (slist[j] in vowels) and (slist[i] in vowels):
                # switch
                temp = slist[j]
                slist[j] = slist[i]
                slist[i] = temp
                j-=1
                i+=1
        return "".join(slist)
