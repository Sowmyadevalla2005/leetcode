class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        for i in range(n):
            if pow(2,i)==n:
                return True
            elif pow(2,i)>n:
                break
        return False
        