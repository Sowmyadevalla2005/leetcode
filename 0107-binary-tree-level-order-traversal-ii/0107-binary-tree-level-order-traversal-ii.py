# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        q=deque([root])
        if not root:
            return []
       
        while q:
            length=len(q)
            ians=[]

            for _ in range(length):
                node=q.popleft()
                ians.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            ans.append(ians)
        return list(reversed(ans))


        