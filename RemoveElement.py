class Solution:
    def removeElement(self, A, elem):
        if len(A) == 0:
            return 0
        end = 0
        for i in A:
            if i != elem:
                A[end] = i
                end += 1
        return end

def main():
    test = Solution()
    print test.removeElement([1,2,2], 2)

if __name__ == "__main__":
    main()
