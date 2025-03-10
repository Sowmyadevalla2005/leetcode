class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)-1):
            stones.sort(reverse=True)
            if len(stones)<2:
                break
            x=stones[0]
            y=stones[1]

            if x!=y:
                s=x-y
                stones=stones[2:]+[s]
            else:
                stones=stones[2:]
        return stones[0] if stones else 0


        