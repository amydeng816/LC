class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        d = {}
        for row in board:
            for i in row:
                if i != '.':
                    if i in d:
                        return False
                    else:
                        d[i] = True
            d = {}
        pos = 0
        d = {}
        while pos < len(board):
            for row in board:
                if row[pos] != '.':
                    if row[pos] in d:
                        return False
                    else:
                        d[row[pos]] = True
            pos += 1
            d = {}
        for r in range(3):
            for c in range(3):
                if not self.isValidPart(board, r * 3, c * 3):
                    return False
        return True
    def isValidPart(self, board, row, col):
        r = row
        d = {}
        while r < row + 3:
            c = col
            while c < col + 3:
                if board[r][c] != '.':
                    if board[r][c] in d:
                        return False
                    else:
                        d[board[r][c]] = True
                c += 1
            r += 1
            d = {}
        return True

def main():
    test = Solution()
    print test.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])

if __name__ == "__main__":
    main()
