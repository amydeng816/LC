class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for x in tokens:
            if x in ('+','-','*','/'):
                x1 = int(stack.pop())
                x2 = int(stack.pop())
                if x == '+':
                    stack.append(str(x2 + x1))
                if x == '-':
                    stack.append(str(x2 - x1))
                if x == '*':
                    stack.append(str(x2 * x1))
                if x == '/':
                    stack.append(str(int(1.0*x2 / x1)))
            else:
                stack.append(x)
        return int(stack.pop())