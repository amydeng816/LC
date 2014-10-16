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
        min_depth = float("inf")
        l = [root]
        depths = [1]
        while l:
            temp_node = l.pop()
            temp_depth = depths.pop()
            if temp_node.left == None and temp_node.right == None:
                if temp_depth < min_depth:
                    min_depth = temp_depth
            if temp_node.left != None:
                l.append(temp_node.left)
                depths.append(temp_depth + 1)
            if temp_node.right != None:
                l.append(temp_node.right)
                depths.append(temp_depth + 1)
        return min_depth