class Solution:
    def calculates(self, s: str) -> int:
        operands,operators=[],[]
        # clean the input
        s = s.strip()
        index=0
        while index < (len(s)):
            char = s[index]
            if not char or char ==" ":
                index+=1
                continue
            if char in ["*","/"]:
                while s[index] in ["*","/"," "]:
                    index+=1
                prevElem = operands.pop()
                if char == "*":
                    operands.append(int(prevElem) * int(s[index]))
                else:
                    operands.append(int(prevElem) // int(s[index]))
                
                
                print(operands)
            elif char in ["+","-"]:
                operators.append((char))
                # index+=1
            else :
                operands.append(int(char))
                # index+=1
            index+=1
        print(operators,operands)
        if len(operands)>1 and not operators:
            return int(s)
        # perform the operations
        while  operators:
            operator = operators.pop()
            operand2,operand1 = operands.pop(),operands.pop()
            if operator == "+":
                result = operand1 + operand2
            if operator == "-":
                result = operand1 - operand2
            if operator == "*":
                result = operand1 * operand2
            if operator == "/":
                result = operand1 // operand2
            operands.append(result)
        return operands[-1]
    def calculate(self,s: str) -> int:
        if not s:
            return 0
        
        stack = []
        current_number = 0
        operation = '+'
        len_s = len(s)

        for i in range(len_s):
            current_char = s[i]

            if current_char.isdigit():
                current_number = (current_number * 10) + int(current_char)

            if not current_char.isdigit() and not current_char.isspace() or i == len_s - 1:
                if operation == '-':
                    stack.append(-current_number)
                elif operation == '+':
                    stack.append(current_number)
                elif operation == '*':
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    stack.append(int(stack.pop() / current_number))
                
                operation = current_char
                current_number = 0

        return sum(stack)