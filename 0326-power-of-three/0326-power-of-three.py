class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n!=1 and n>2:
            n=n/3
        if n==1:
            return True
        else:
            return False
        