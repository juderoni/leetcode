class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # get smalles len string of list
        lenting = len(strs[0])
        for i in strs:
            if (lenting > len(i)):
                lenting = len(i)
            if i == "":
                return ""
        
        # now iteratively check the latters that match
        comparStr = ""
        for i in range(lenting):
            comparStr += strs[0][i]
            for tingy in strs:
               
                if comparStr != tingy[:i + 1]:
                    return comparStr[:i]
        return comparStr


 

