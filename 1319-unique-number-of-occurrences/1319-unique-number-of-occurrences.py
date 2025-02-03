class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurance_count={}
        for i in arr:
            if i in occurance_count:
                occurance_count[i]+=1
            else:
                occurance_count[i]=1

        count=set()

        for value in occurance_count.values():
            if value in count:
                return False
            count.add(value)
        return True

        