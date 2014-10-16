class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printAllPaths(root, target):
    if root == None:
        return []
    solutions = []
    printAllPathHelp(root, target, solutions)
    return solutions

def printAllPathHelp(root, target, solutions):
    if root == None:
        return
    printAllPathsRec(root, target, 0, [], solutions)
    printAllPathHelp(root.left, target, solutions)
    printAllPathHelp(root.right, target, solutions)

def printAllPathsRec(node, target, tempSum, tempList, solutions):
    if node == None:
        return
    tempList.append(node.val)
    tempSum += node.val
    if tempSum == target:
        solutions.append(list(tempList))
    printAllPathsRec(node.left, target, tempSum, tempList, solutions)
    printAllPathsRec(node.right, target, tempSum, tempList, solutions)
    tempList.pop()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(3)
r = root.right
r.left = TreeNode(0)
r.left.left = TreeNode(1)
r.right = TreeNode(2)
r.right.left = TreeNode(0)
r.right.left.left = TreeNode(1)
r.right.left.right = TreeNode(1)
print printAllPaths(root, 3)
