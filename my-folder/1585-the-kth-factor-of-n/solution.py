class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        retlist = []
        for i in range(1,n+1):
            if n % i == 0:
                retlist.append(i)
        if len(retlist) >= k:
            return retlist[k-1]
        return -1
        
