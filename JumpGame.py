class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        maxReach = 0
        for i in range(len(A)):
            if i > maxReach:
                return False
            if i + A[i] > maxReach:
                maxReach = i + A[i]
        return True
            