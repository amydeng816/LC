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
        l1 = [p]
        l2 = [q]
        while l1 and l2:
            t1 = l1.pop()
            t2 = l2.pop()
            if t1.val != t2.val:
                return False
            if (t1.left == None and t2.left != None) or (t1.left != None and t2.left == None) or (t1.right == None and t2.right != None) or (t1.right != None and t2.right == None):
                return False
            if t1.left != None:
                l1.append(t1.left)
                l2.append(t2.left)
            if t1.right != None:
                l1.append(t1.right)
                l2.append(t2.right)
        return True

def main():
    t1 = TreeNode(1)
    t1.left = TreeNode(0)
    t1.right = TreeNode(2)
    t2 = TreeNode(1)
    t2.left = TreeNode(0)
    t2.right = TreeNode(2)
    test = Solution()
    print test.isSameTree(t1, t2)

if __name__ == "__main__":
    main()
