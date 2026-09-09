class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def oper(a, b, op):
            if op == "+":
                return a + b
            if op == "-":
                return a - b
            if op == "*":
                return a * b
            if op == "/":
                return int(a / b)

        for token in tokens:

            if token not in "+-*/":
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(oper(a, b, token))

        return stack[-1]