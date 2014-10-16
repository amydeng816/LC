class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        return self.sortedArrayToBSTRec(num, 0, len(num) - 1)
    def sortedArrayToBSTRec(self, num, low, high):
        if low > high:
            return None
        mid = (low + high) / 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBSTRec(num, low, mid - 1)
        root.right = self.sortedArrayToBSTRec(num, mid + 1, high)
        return root

def main():
    test = Solution()
    print test.sortedArrayToBST([1, 2, 3]).left.val

if __name__ == "__main__":
    main()
