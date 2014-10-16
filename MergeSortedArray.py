class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if not A:
            A = B
            return
        if not B:
            return
        i = m + n - 1
        while m > 0 and n > 0:
            if A[m - 1] >= B[n - 1]:
                A[i] = A[m - 1]
                m -= 1
            else:
                A[i] = B[n - 1]
                n -= 1
            i -= 1
        while n > 0:
            A[i] = B[n - 1]
            n -= 1
            i -= 1