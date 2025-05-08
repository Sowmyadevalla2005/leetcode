# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return []
        bfs=[]
        minDiff = float('inf')

        q=deque([root])
        while q:
            length=len(q)
            

            for _ in range(length):
                node=q.popleft()
                bfs.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        bfs.sort()
        minDiff=float('inf')
        for i in range(1,len(bfs)):
            Diff=abs(bfs[i]-bfs[i-1])
            if Diff<minDiff:
                minDiff=Diff
        return minDiff

            



        