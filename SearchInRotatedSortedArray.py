class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        return self.searchR(A, target, 0, len(A) - 1)
        
    def searchR(self, A, target, begin, end):
        if end < begin:
            return -1
        
        if end == begin and A[end] == target:
            return end
        
        mid = (begin + end) / 2;
        if A[mid] == target:
            return mid
        if A[begin] < A[mid] and target <= A[mid] and target >= A[begin]:
            return self.searchR(A, target, begin, mid - 1)
        if A[mid] < A[end] and target <= A[end] and target >= A[mid]:
            return self.searchR(A, target, mid + 1, end)
        if A[begin] > A[mid]:
            return self.searchR(A, target, begin, mid - 1)
        if A[mid] > A[end]:
            return self.searchR(A, target, mid + 1, end)
        return -1