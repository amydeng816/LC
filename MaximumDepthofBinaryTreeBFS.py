class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        l = [root]
        depth = 0
        temp = []
        while l:
            while l:
                node = l.pop()
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            l = temp
            temp = []
            depth += 1
        return depth

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
