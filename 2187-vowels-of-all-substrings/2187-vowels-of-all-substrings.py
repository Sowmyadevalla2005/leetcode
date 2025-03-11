class Solution:
    def countVowels(self, word: str) -> int:
        total, cnt_substrig = 0, 0
        for i, ch in enumerate(word, 1):
            if ch in {'a', 'e', 'i', 'o', 'u'}:
                cnt_substrig += i
            total += cnt_substrig
        return total    