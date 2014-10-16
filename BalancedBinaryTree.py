# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.depth(root) != -1
    def depth(self, node):
        if node == None:
            return 0
        left = self.depth(node.left)
        if left == -1:
            return -1
        right = self.depth(node.right)
        if right == -1:
            return -1
        diff = abs(left - right)
        if diff > 1:
            return -1
        return 1 + max(left, right)