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

        def post(root):
            if root:
                for c in root.children:
                    post(c)
                res.append(root.val)
        post(root)
        return res
                
            
                  