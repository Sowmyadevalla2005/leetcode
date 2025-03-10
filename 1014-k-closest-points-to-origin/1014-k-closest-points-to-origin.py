import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        r=[]
        for i in points:
            s=math.sqrt(i[0]**2+i[1]**2)
            l.append(s)
        poin_s=list(zip(points,l))
        poin_s.sort(key=lambda x:x[1])
    
        for i in range(k):
            r.append(poin_s[i][0])
        return r


        