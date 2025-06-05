# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
      
        self.sum_max=float('-inf')
        def post_order(node):
            
            if not node:
                return 0

            left=max(0,post_order(node.left))
            right=max(0,post_order(node.right))
            self.sum_max = max(self.sum_max,node.val+left+right)

            return node.val+max(left,right)
        post_order(root)
        return self.sum_max
