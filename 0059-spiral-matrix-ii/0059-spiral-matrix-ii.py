class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0]*n  for _ in range(n)]

        top,bottom,left,right = 0,n-1,0,n-1

        num=1

        while(num<=n*n):
            for i in range(left,right+1):
                matrix[top][i]=num
                num+=1
            top+=1

            for j in range(top,bottom+1):
                matrix[j][right]=num
                num+=1
            right-=1

            if (top<=bottom):
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=num
                    num+=1
                bottom-=1
        
            if (left<=right):
                for j in range(bottom,top-1,-1):
                    matrix[j][left]=num
                    num+=1
                left+=1
    
        return matrix

        