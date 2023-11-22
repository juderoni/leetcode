class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenStr = len(strs[0])
        bing = strs[0]
        for i in strs:
            leni = len(i)
            if lenStr > leni:
                lenStr = leni
        
        for i in range(0,1+ lenStr):
            correct = True
            for val in strs:
                if bing[0:(lenStr - i)] in val[0:(lenStr - i)]:
                    
                    continue
                else:
                    correct = False
                    continue
            if (correct):
                return bing[0:lenStr - i]
        return ""
