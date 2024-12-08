class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(100000)
        res=''.join(map(str,num))
        sum=int(res)+k
        arr=[int(digit) for digit in str(sum)]
        return arr


        