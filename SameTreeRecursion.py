class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def main():
    t1 = TreeNode(1)
    t1.left = TreeNode(0)
    t1.right = TreeNode(2)
    t2 = TreeNode(1)
    t2.left = TreeNode(0)
    t2.right = TreeNode(3)
    test = Solution()
    print test.isSameTree(t1, t2)

if __name__ == "__main__":
    main()
