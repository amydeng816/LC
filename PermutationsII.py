class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        solutions = []
        self.permuteUniqueRec(num, solutions, [])
        return solutions
    def permuteUniqueRec(self, num, solutions, tempList):
        if len(num) == 0:
            solutions.append(list(tempList))
            return
        for i in range(len(num)):
            if (i == 0) or (i > 0 and num[i - 1] != num[i]):
                print '-------'
                print i
                tempList.append(num[i])
                print num[:i]
                print num[i + 1:]
                self.permuteUniqueRec(num[:i] + num[i + 1:], solutions, tempList)
                tempList.pop()

def main():
    s = Solution()
    print s.permuteUnique([-1, 2, -1])
if __name__ == "__main__":
    main()
