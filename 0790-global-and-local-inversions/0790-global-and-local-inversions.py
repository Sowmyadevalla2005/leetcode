class Solution:
  def isIdealPermutation(self, A: List[int]) -> bool:

        for i, num in enumerate(A):
     
            if abs(i - num) > 1:
                return False
        return True