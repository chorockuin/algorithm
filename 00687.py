# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def travel(node):
            if node is None:
                return 0

            left = -1
            right = -1
            lv = rv = -999999

            if node.left:
                left, lv = travel(node.left)
            if node.right:
                right, rv = travel(node.right)
            if lv == node.val and rv == node.val:
                self.max_len = max(self.max_len, left + right + 2)
                return max(left, right) + 1, node.val
            else:
                if lv == node.val:
                    self.max_len = max(self.max_len, left + 1)
                    return left + 1, node.val
                if rv == node.val:
                    self.max_len = max(self.max_len, right + 1)
                    return right + 1, node.val
            return 0, node.val

        self.max_len = 0
        travel(root)
        return self.max_len
