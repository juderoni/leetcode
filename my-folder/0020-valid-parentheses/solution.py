class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ["{", "[", "("]
        right = ["}", "]", ")"]
        mapi = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for i in s:
            if i in left:
                stack.append(i)
            elif i in right:
                if len(stack) == 0:
                    return False
                leftting = stack.pop()
                lefttingmatch = mapi[i]
                
                if leftting != lefttingmatch:
                    return False
        if len(stack) != 0:
            return False
        return True
