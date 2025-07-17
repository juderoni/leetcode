class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # basically. 
        # len of consecutive even or odds
        # len of consectuive alternating
        binList = []
        for i in nums:
            binList.append(i % 2)
        
        lenEvenMax = 0
        lenOddMax = 0
        lenAltMax = 1

        # count evens, count odds
        for i in binList:
            if i == 0:
                lenEvenMax += 1
            if i == 1:
                lenOddMax += 1
        
        # count alternating
        temp = binList[0]
        for i in binList[1:]:
            if i == temp:
                continue
            else:
                temp = i
                lenAltMax += 1
            
        return max(lenAltMax, lenEvenMax, lenOddMax)




        
                
        
    
            




