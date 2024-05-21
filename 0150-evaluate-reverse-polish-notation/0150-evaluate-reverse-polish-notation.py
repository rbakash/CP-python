class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                rightOperand = stack.pop()
                leftOperand = stack.pop()

                value = eval("".join(str(leftOperand) + token + str(rightOperand)))
                stack.append(int(value))

        return int(stack[-1])
