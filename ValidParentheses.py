class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')':
                    if stack.pop() != '(':
                        return False
                if i == '}':
                    if stack.pop() != '{':
                        return False
                if i == ']':
                    if stack.pop() != '[':
                        return False
        return len(stack) == 0