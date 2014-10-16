class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        l = [1]
        for i in range(1, rowIndex + 1):
            l_temp = [1]
            for ptr in range(1, len(l)):
                l_temp.append(l[ptr] + l[ptr - 1])
            l_temp.append(1)
            l = l_temp
        return l