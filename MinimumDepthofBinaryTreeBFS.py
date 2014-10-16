# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        depth = 1
        l = [root]
        temp = []
        while l:
            while l:
                node = l.pop()
                if node.left == None and node.right == None:
                    return depth
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            l = temp
            temp = []
            depth += 1
        return depth