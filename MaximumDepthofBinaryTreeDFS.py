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
        max_depth = 1
        depth = [1]
        while l:
            temp_node = l.pop()
            temp_depth = depth.pop()
            new_depth = temp_depth + 1
            if temp_node.left != None:
                l.append(temp_node.left)
                depth.append(new_depth)
                if new_depth > max_depth:
                    max_depth = new_depth
            if temp_node.right != None:
                l.append(temp_node.right)
                depth.append(new_depth)
                if new_depth > max_depth:
                    max_depth = new_depth
        return max_depth

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
