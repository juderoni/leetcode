class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # want to know if the intersection of the two strings is real
        j = 0
        if len(s) == 0:
            return True
        
        for i in t:
            if i == s[j]:
                j += 1
            if j == len(s):
                return True

        return False

