# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans=[]
        q=deque([root])

        while q:
            length=len(q)

            inans=[]
            level = 0
            for _ in range(length):
                node=q.popleft()
                inans.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level+=1

            ans.append(inans)
        res=[]
        for i in range(len(ans)):
            if i%2==0:
                res.append(ans[i])
            else:
                res.append(ans[i][::-1])
        return res
        
    

        