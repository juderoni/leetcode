class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        counter = 0
        for i in reversed(range(len(s))):
            if (s[i] != " "):
                counter+=1
            else:
                return counter
        return counter
