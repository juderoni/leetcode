class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # march 1 letter at a time and go until we see a duplicate
        longest = 0
        for i, item in enumerate(s):
            setTracker = set()
            localLen = 0
            hit = False
            for j in range(i, len(s)):
                #print(s[j])
                setTracker.add(s[j])
                tmp = localLen
                localLen = len(setTracker)
                # print(localLen)
                #print(tmp)
                #print(localLen)
                if tmp == localLen:
                    longest = max(longest, tmp)
                # print(longest)
                    hit = True
                    break
            if not hit:
                longest = max(longest, localLen)
            
        return longest


