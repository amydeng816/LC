class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def main():
    t1 = TreeNode(1)
    t1.left = TreeNode(0)
    t1.right = TreeNode(0)
    t1.left.right = TreeNode(3)
    t1.left.right.left = TreeNode(3)
    test = Solution()
    print test.maxDepth(t1)

if __name__ == "__main__":
    main()
