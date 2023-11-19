class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        if (x == 0):
            return True
        rev = 0
        temp = x
        while temp > 9:
            ting = temp % 10
            rev += ting
            temp /= 10
            temp = int(temp)
            rev *= 10
        rev += temp

        if (rev == x):
            return True
        else:
            return False
        
        
