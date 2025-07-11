class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rtnStr = ""
        # zig zag pattern
        # abcdefghijk
        # 01232101232
        # 0 a.   g
        # 1 b. f h
        # 2 c e. i k
        # 3 d.   j
        if numRows >= len(s) or numRows == 1:
            return s

        # n = 4, so you want to go from 0 - 3
        # i want to make that list, which tells me where to put letters
        #make list
        lenString = len(s)
        numList = []
        idx = 0
        adder = 1
        goingDown = False
        for i in range(lenString):
            numList.append(idx)
            idx += adder
            if not goingDown and idx == numRows - 1:
                goingDown = True
                adder = -1
            elif goingDown and idx == 0:
                goingDown = False
                adder = 1
        
        # now should have a list 0123210
        rtnList = []
        print(numList)
        for i in range(numRows):
            rtnList.append([])
        
        for i, item in enumerate(numList):
            rtnList[item].append(s[i])
        
        for i in rtnList:
            for j in i:
                rtnStr += j

        return rtnStr
            


        # want to print 0 first then 1 and so on.
        # return list, will be double list.
        # number of items (which are list) = to numRows
        

        
