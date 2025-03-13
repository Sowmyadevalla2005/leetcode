class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m=len(grid)
        n=len(grid[0])

        p=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    p+=4
                    if i<m-1 and grid[i+1][j]==1:
                        p=p-2
                    if  j<n-1 and grid[i][j+1]==1:
                        p=p-2
        return p
        