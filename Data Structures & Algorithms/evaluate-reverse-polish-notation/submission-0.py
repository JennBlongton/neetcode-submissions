class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        operands = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "*":
                    res = a * b
                elif token == "/":
                    # Division should truncate toward zero
                    res = int(a / b)

                stack.append(res)

        return stack[-1]

