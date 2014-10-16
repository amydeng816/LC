class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        solutions = []
        self.generateParenthesisRec('', solutions, n, 0)
        return solutions
    def generateParenthesisRec(self, s, solutions, n, left):
        if n == 0 and left == 0:
            solutions.append(s)
            return
        if n == 0 and left > 0:
            s = s + ")"
            self.generateParenthesisRec(s, solutions, n, left - 1)
        elif n > 0 and left == 0:
            s = s + "("
            self.generateParenthesisRec(s, solutions, n - 1, left + 1)
        else:
            s = s + ")"
            self.generateParenthesisRec(s, solutions, n, left - 1)
            s = s[:len(s) - 1]
            s = s + "("
            self.generateParenthesisRec(s, solutions, n - 1, left + 1)