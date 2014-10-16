class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetricTree(self, root):
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        l1 = [root.left]
        l2 = [root.right]
        while l1 and l2:
            t1 = l1.pop()
            t2 = l2.pop()
            if t1.val != t2.val:
                return False
            if (t1.left == None and t2.right != None) or (t1.left != None and t2.right == None) or (t1.right == None and t2.left != None) or (t1.right != None and t2.left == None):
                return False
            if t1.left != None:
                l1.append(t1.left)
                l2.append(t2.right)
            if t1.right != None:
                l1.append(t1.right)
                l2.append(t2.left)
        return True

def main():
    t1 = TreeNode(1)
    t1.left = TreeNode(0)
    t1.right = TreeNode(0)
    t1.left.right = TreeNode(3)
    t1.right.left = TreeNode(2)
    test = Solution()
    print test.isSymmetricTree(t1)

if __name__ == "__main__":
    main()
