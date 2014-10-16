class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 3:
            return len(A)
        low = 0
        high = 1
        count = 1
        while high < len(A):
            if A[high] == A[low]:
                if count < 2:
                    low += 1
                    A[low] = A[high]
                count += 1
            else:
                low += 1
                A[low] = A[high]
                count = 1
            high += 1
        return low + 1