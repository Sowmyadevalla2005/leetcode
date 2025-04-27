# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        if root.left:
            left=self.minDepth(root.left)
        else:
            left=float('inf')
            
        if root.right:
            right=self.minDepth(root.right)
        else:
            right=float('inf')

        return 1+min(left,right)


