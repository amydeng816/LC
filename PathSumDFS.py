# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        node_list = [root]
        sum_list = [root.val]
        while node_list:
            temp = node_list.pop()
            s = sum_list.pop()
            if temp.left == None and temp.right == None:
                if s == sum:
                    return True
                else:
                    continue
            if temp.left != None:
                node_list.append(temp.left)
                sum_list.append(s + temp.left.val)
            if temp.right != None:
                node_list.append(temp.right)
                sum_list.append(s + temp.right.val)
        return False