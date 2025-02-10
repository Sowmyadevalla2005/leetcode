class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X=0
        for o in operations:
            if o=='--X':
                X-=1
            elif o=='X--':
                X-=1
            elif o=='++X':
                X+=1
            elif o=='X++':
                X+=1
        return X

