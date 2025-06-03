"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        res=[]
        stack=[root]

        while stack:
            c=stack.pop()
            res.append(c.val)
            for t in c.children:
                stack.append(t)
        return list(reversed(res))      