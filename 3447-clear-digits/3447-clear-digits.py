class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=[]
        for i in s:
            if i.isdigit():
                d.pop()
            else:
                d.append(i)
        return "".join(d)
        