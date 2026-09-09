class Solution:
    def isValid(self, s: str) -> bool:
        comp = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for i in s:
            if (stack) and (stack[-1] == comp.get(i)):
                stack.pop()
            else:
                stack.append(i)    

        return not stack   
