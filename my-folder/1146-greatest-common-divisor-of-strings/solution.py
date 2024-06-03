class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 == str2):
            return str1
        if (len(str1) > len(str2)):
            return self.ting(str2, str1)
        else:
            return self.ting(str1, str2)
    

    def ting(self, smaller: str, bigger: str) -> str:
        for i in reversed(range(1, len(smaller) + 1)):
            
            if (smaller[:i] == bigger[:i] and len(bigger) % i == 0 and len(smaller) % i ==0):
                num1 = int(len(bigger) / i)
                num2 = int(len(smaller) / i)
                
                tingstring = smaller[:i]
                if(tingstring * num2 == smaller and tingstring * num1 == bigger):
                    return tingstring
        return ""

        
        
