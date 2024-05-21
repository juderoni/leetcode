class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        justPlaced = False
        count = 0
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and (not justPlaced) and (len(flowerbed) - 1) != i and flowerbed[i + 1] == 0) :
                count+=1
                justPlaced = True
            elif flowerbed[i] == 1:
                justPlaced = True
            elif (len(flowerbed) - 1) == i and (not justPlaced) and flowerbed[i] == 0:
                count+=1
                
            else:
                justPlaced = False
        if count >= n:
            return True
        else:
            return False
