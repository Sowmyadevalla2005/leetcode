# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None

        r_val = postorder.pop()
        root = TreeNode(r_val)
        ind = inorder.index(r_val)

        root.right = self.buildTree(inorder[ind+1:],postorder)
        root.left = self.buildTree(inorder[0:ind],postorder)
        return root



        