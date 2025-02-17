class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        k1 = 0
        for i in range(1, n + 1):
            if n % i == 0:
                k1+=1
            if k1 == k:
                return i
        return -1
        
