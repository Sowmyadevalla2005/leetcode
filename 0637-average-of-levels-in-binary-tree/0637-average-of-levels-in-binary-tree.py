# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return 
        q=deque([root])
        ans=[]
        s=[]

        while q:

            length = len(q)

            ians=[]
            for _ in range(length):
                node=q.popleft()
                ians.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(ians)
        for i in ans:
            p=sum(i)*1.0/len(i)
            s.append(p)
        return s
        



        