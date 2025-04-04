# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a = {}

    def trav(self, root, d):
        if root:
            self.trav(root.left, d + 1)
            self.a[d] = root.val
            self.trav(root.right, d + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.a = {}
        self.trav(root, 0)
        return [self.a[i] for i in sorted(self.a)]