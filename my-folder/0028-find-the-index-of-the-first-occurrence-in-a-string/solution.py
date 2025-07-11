class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # basically we want to keep a save of len(needle) chars as we progress through the haystack. and check whehther or not the window == needle. return first index of the window
        windowString = ""
        for i in range(0, len(haystack)):
            if len(windowString) != len(needle):
                windowString += haystack[i]
                continue
            print(windowString)
            
            if windowString == needle:
                return i - len(needle)
            # now we have len(windowString == len(needle))
            windowString = windowString[1:]
            windowString += haystack[i]
        if windowString == needle:
            return len(haystack) - len(needle)
        return -1
            
