class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A == None:
            return 0
        start = -1
        end = len(A)
        while end - start > 1:
            mid = start + (end - start) / 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        return end