class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        al=[0]
        for j in range(len(gain)):
            s=al[j]+gain[j]
            al.append(s)
        return max(al)
        