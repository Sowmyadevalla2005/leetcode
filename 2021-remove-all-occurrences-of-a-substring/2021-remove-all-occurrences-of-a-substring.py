class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """

        d=''
        for i in range(len(s)):
            d=d+s[i]
            if part in d:
                d=d.replace(part,'')
        return d