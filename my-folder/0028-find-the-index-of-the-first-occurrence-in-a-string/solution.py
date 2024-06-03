class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, item in enumerate(haystack):
            if item == needle[0]:
                for j in range(0, len(needle)):
                    if len(haystack) <= i + j or haystack[i + j] != needle[j]:
                        break
                    elif len(haystack) <= i + j:
                        break
                    elif j == len(needle) - 1 and haystack[i + j] == needle[j]:
                        return i
        return -1
