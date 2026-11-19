# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root

        ppath = self.bs(root, p, {})
        qpath = self.bs(root, q, {})

        print("ppath:", {key: node.val for key, node in ppath.items()})
        print("qpath:", {key: node.val for key, node in qpath.items()})

        merged = zip(ppath.values(), qpath.values())
        last_valid = 0

        for p,q in merged:
            if p==q:
                last_valid += 1
            else:
                break

        return ppath[last_valid]
    
        #print("qpath keys:", list(qpath))
        #print("qpath stored node values:", [node.val for node in qpath.values()])
        #for x in ppath:
        #    print("x:", x, "type:", type(x).__name__)

        return TreeNode()

    def bs(self, root: TreeNode, elem: TreeNode, path: dict[int, TreeNode]) -> dict[int, TreeNode]:
        #print("visiting:", root.val, "looking for:", elem.val)
        num = len(path) + 1
        path[num] = root

        if root is elem:
            return path
        if root.val > elem.val:
            return self.bs(root.left, elem, path)
        else:
            return self.bs(root.right, elem, path)