# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left:
            l=self.maxDepth(root.left)
        else:
            l= 0
        if root.right:
            r=self.maxDepth(root.right)
        else:
            r=0

        return 1+max(l,r)