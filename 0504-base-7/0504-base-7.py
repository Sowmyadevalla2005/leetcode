class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num==0:
            return "0"
        if num<0:
            sign = "-"
        else:
            sign=""
        num=abs(num)
        res=""
        while num:
            res=str(num%7)+res
            num=num//7
        return sign+res

        