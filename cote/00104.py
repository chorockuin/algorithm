# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.max_depth = 0
        self.travel(root, 1)
        return self.max_depth

    def travel(self, node, depth):
        if node is None:
            return 0

        if node.left:
            self.travel(node.left, depth + 1)
        if node.right:
            self.travel(node.right, depth + 1)
        if depth > self.max_depth:
            self.max_depth = depth


root = [3,9,20,None,None,15,7]

print(Solution().maxDepth(root))