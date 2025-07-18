class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aioue"
        isVowelList = []
        maxCounter = 0
        for i in range(0, k):
            if s[i] in vowels:
                maxCounter += 1
                isVowelList.append(1)
            else:
                isVowelList.append(0)
        leftover = 0
        counter = maxCounter
        for i in range(k, len(s)):
            if s[i] in vowels:
                counter+=1
                isVowelList.append(1)
            else:
                isVowelList.append(0)
            if isVowelList[leftover] == 1:
                counter-=1
            leftover+=1
            maxCounter = max(maxCounter, counter)
        print(isVowelList)
        return maxCounter

