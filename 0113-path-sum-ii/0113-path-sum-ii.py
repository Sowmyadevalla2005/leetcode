# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        s=[]
        def dfs(node,curr):
            if not node:
                return 
            cur=curr+[node.val]

            if not node.left and not node.right:
                if sum(cur)==targetSum:
                    s.append(cur)
                return
            dfs(node.left,cur)
            dfs(node.right,cur)
        dfs(root,[])
        return s

        