class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        p=[[1]]

        for i in range(1,numRows):
            s=[1]
            for j in range(1,i):
                s.append(p[i-1][j-1]+p[i-1][j])
            s.append(1)
            p.append(s)
        return p        