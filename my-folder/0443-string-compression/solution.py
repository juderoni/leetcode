class Solution:
    def compress(self, chars: List[str]) -> int:
        localLen = 1
        lastSeenChar = chars[0]
        rtnList = []
        # basically we want to count how many repeating chars there are for every item in this list. If one, just append, if more, don't append until we see new. We will print everytime we see a new unique char, or end of loop
        i = 1
        while i < len(chars):
            
            if lastSeenChar != chars[i]:
                rtnList.append(lastSeenChar)
                if localLen != 1:
                    for j in str(localLen):
                        rtnList.append(f"{j}")
                localLen = 1
                lastSeenChar = chars[i]
            else:
                localLen += 1
            print(rtnList)
            i+=1
        rtnList.append(lastSeenChar)
            
        if localLen != 1:
            for i in str(localLen):
                rtnList.append(f"{i}")
        
        for i, item in enumerate(rtnList):
            chars[i] = item
        
        return len(rtnList)

