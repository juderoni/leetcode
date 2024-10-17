class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subi = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            
            if s[subi] == t[i]:
                subi += 1
            if subi == len(s):
                return True
        return False
            
