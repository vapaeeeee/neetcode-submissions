from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        visited = []
        current_level = []
        nodes_left_in_level = len(queue)

        while queue:
            node = queue.popleft()
            current_level.append(node.val)
            nodes_left_in_level -= 1

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            if nodes_left_in_level == 0:
                visited.append(current_level)
                current_level = []
                nodes_left_in_level = len(queue)

        return visited

        
    def bfs(self, root:Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = deque([root])
        visited = []

        while queue:
            node = queue.popleft()
            visited.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        return visited