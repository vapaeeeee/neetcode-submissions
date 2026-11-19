# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        low = min(p.val, q.val)
        high = max(p.val, q.val)
        current = root

        while True:
            if current.val < low:
                current = current.right
            elif current.val > high:
                current = current.left
            else:
                return current
