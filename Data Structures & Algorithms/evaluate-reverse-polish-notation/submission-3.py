class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:

            if t == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 + op2)

            elif t == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            
            elif t == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 * op2)
            
            elif t == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(float(op2) / op1))
            
            else:
                stack.append(int(t))
        
        return stack[-1]