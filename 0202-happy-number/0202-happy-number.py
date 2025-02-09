class Solution:
    def isHappy(self, n: int) -> bool:
        used = []
        while n != 1 : 
            new_n = 0
            for i in str(n) : 
                new_n += int(i)**2
            n = new_n
            if n not in used: 
                used.append(n)
            else : 
                return False
        return True