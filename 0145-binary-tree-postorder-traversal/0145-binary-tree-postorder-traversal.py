class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res=[]
        st=[root]
        if root is None:
            return []

        while st:
            node = st.pop()
            if node:
                st.append(node.left)
                st.append(node.right)
                res.append(node.val)
        return list(reversed(res))