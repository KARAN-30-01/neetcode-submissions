class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        def oper(c,d,op):
            

            if op == "+":
                return int(c+d)
            if op == "-":
                return int(c-d)
            if op == "*":
                return int(c*d)
            if op == "/":
                return int(c/d)


        for i in tokens :
            
            if i not in "+-*/":
                stack.append(int(i))       

            else:
                b=stack.pop()
                a=stack.pop()
                stack.append(oper(a,b,i))

        return int(stack[-1])        

