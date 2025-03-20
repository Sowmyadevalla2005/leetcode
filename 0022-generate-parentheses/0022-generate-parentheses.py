class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res,sol=[],[]

        def backtrack(openn,close):
            if len(sol)==2*n:
                res.append("".join(sol))
                return
            
            if openn<n:
                sol.append("(")
                backtrack(openn+1,close)
                sol.pop()
            
            if openn>close:
                sol.append(")")
                backtrack(openn,close+1)
                sol.pop()
            
        backtrack(0,0)

        return res
        