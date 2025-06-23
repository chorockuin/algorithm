# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_len = 0
        self.travel(root)
        return self.max_len

    def travel(self, node):
        if node is None:
            return 0
        left = -1
        right = -1

        if node.left:
            left = self.travel(node.left)
        if node.right:
            right = self.travel(node.right)
        self.max_len = max(self.max_len, left + right + 2)
        return max(left, right) + 1