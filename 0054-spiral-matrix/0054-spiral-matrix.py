class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top,bottom,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        index=0
        while(top<=bottom and left<=right):

            for j in range(left,right+1):
                res.append(matrix[top][j])
                index+=1
            top+=1

            for i in range(top,bottom+1):
                res.append(matrix[i][right])
                index+=1
            right-=1

            if(top<=bottom):
                for j in range(right,left-1,-1):
                    res.append(matrix[bottom][j])
                    index+=1
                bottom-=1

            if(left<=right):
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                    index+=1
                left+=1
        return res

        
        