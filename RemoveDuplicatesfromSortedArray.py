class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        end = 0
        for i in A:
            if i != A[end]:
                end += 1
                A[end] = i
        return end + 1

def main():
    test = Solution()
    print test.removeDuplicates([1,2,2])


if __name__ == "__main__":
    main()
