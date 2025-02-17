class Solution:
    def partitionString(self, s: str) -> int:
        uniquelist = []
        rtn = 1
        for i in s:
            if i not in uniquelist:
                uniquelist.append(i)
            else:
                rtn+=1
                uniquelist = [i]
                
        return rtn

