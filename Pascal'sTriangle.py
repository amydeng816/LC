class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        rows = [[1]]
        for i in range(1, numRows):
            l = [1]
            for ptr in range(1, len(rows[i - 1])):
                l.append(rows[i - 1][ptr] + rows[i - 1][ptr - 1])
            l.append(1)
            rows.append(l)
        return rows