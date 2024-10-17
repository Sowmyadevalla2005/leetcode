class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str=''.join(map(str,digits))
        num=int(num_str)+1
        return [int(x) for x in str(num)]
        
        