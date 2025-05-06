# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.height(root)!=-1

    def height(self,root):
        if not root:
            return 0
        
        l=self.height(root.left)
        r=self.height(root.right)

        if l==-1:
            return -1

        if r==-1:
            return -1

        if abs(l-r)>1:
            return -1
        
        return 1+max(l,r)

        