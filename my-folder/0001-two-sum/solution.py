class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, vali in enumerate(nums):
            hashMap[vali] = i
        for i, vali in enumerate(nums):
            comp = target - vali
            if comp in hashMap and hashMap[comp] != i:
                return [i, hashMap[comp]]


        


            
        
