class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetricTree(self, root):
        if root == None:
            return True
        return self.compare(root.left, root.right)
    def compare(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.compare(p.left, q.right) and self.compare(p.right, q.left)


def main():
    t1 = TreeNode(1)
    t1.left = TreeNode(0)
    t1.right = TreeNode(0)
    t1.left.right = TreeNode(3)
#    t1.right.left = TreeNode(3)
    test = Solution()
    print test.isSymmetricTree(t1)

if __name__ == "__main__":
    main()
