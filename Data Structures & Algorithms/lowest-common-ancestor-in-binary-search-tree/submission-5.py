# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # if p.val < root.val < q.val or q.val < root.val < p.val:
        #     return root

        # low = min(p.val, q.val)
        # high = max(p.val, q.val)
        low, high = p.val, q.val
        if low > high:
            low, high = high, low
        current = root

        while True:
            if current.val < low:
                current = current.right
            elif current.val > high:
                current = current.left
            else:
                return current
