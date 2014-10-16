# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        solutions = []
        self.pathSumRec(root, sum, 0, solutions, [])
        return solutions

    def pathSumRec(self, root, sum, temp_sum, solutions, solution):
        if root == None:
            return
        solution.append(root.val)
        temp_sum = temp_sum + root.val
        if root.right == None and root.left == None:
            if temp_sum == sum:
                solutions.append(list(solution))
        else:
            self.pathSumRec(root.left, sum, temp_sum, solutions, solution)
            self.pathSumRec(root.right, sum, temp_sum, solutions, solution)
        solution.pop()