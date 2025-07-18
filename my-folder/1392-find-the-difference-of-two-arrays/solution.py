class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        retList = []
        setNums1 = set(nums1)
        setNums2 = set(nums2)
        retlist1 = [] # where list of ints in num1, not in nums2
        retlist2 = []# list of ints in nums2, not in nums1
        lenSetNums1 = len(setNums1)
        lenSetNums2 = len(setNums2)
        for i in nums1:
            setNums2.add(i)
            if lenSetNums2 != len(setNums2):
                retlist1.append(i)
                lenSetNums2 = len(setNums2)
        for i in nums2:
            setNums1.add(i)
            if lenSetNums1 != len(setNums1):
                retlist2.append(i)
                lenSetNums1 = len(setNums1)
        
        return [retlist1, retlist2]
