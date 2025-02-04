class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        cnt = 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, n):
            if is_prime[i]:
                cnt += 1
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return cnt
