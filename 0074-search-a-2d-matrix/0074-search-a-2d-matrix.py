class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])

        s=m*n
        l=0
        r=s-1

        while l<=r:

            mid=(l+r)//2
            m_i=mid//n
            m_j=mid%n

            if target == matrix[m_i][m_j]:
                return True
            
            elif target < matrix[m_i][m_j]:
                r = mid-1

            else:
                l = mid+1

        return False




        