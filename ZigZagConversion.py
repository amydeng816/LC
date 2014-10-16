class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        newS = ''
        for i in range(min(nRows, len(s))):
            position = i
            convex = False
            while position < len(s):
                newS = newS + s[position]
                if i == 0 or i == nRows - 1:
                    position = position + 2 * nRows - 2
                elif convex == False:
                    convex = True
                    position = position + 2 * (nRows - 1 - i)
                else:
                    convex = False
                    position = position + 2 * i
        return newS