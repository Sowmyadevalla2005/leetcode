class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split()
        reverse_w=words[::-1]
        return ' '.join(reverse_w)