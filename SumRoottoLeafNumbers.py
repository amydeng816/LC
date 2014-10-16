# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        number = [0]
        self.sumNumbersRec(root, number, 0)
        return number[0]
    def sumNumbersRec(self, root, number, s):
        if root == None:
            return
        s = s * 10 + root.val
        if root.left == None and root.right == None:
            number[0] += s
        else:
            self.sumNumbersRec(root.left, number, s)
            self.sumNumbersRec(root.right, number, s)
        s = s / 10