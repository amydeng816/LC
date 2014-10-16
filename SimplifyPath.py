class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        l = path.split("/")
        stack = []
        for x in l:
            if x == '' or x == '.':
                pass
            elif x  == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        s = ''
        if stack:
            for c in stack:
                s = s + '/' + c
        else:
            s = '/'
        return s