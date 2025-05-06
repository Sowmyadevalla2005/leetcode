# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def inn(root):
            if not root:
                return
            else:
                inn(root.left)
                inn(root.right)
                root.left,root.right=root.right,root.left
            
        inn(root)
        return root
        