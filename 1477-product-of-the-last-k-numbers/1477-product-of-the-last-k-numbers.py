class ProductOfNumbers(object):

    def __init__(self):
        self.l=[]
        self.p=[1]
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num==0:
            self.l=[]
            self.p=[1]
        else:
            self.l.append(num)
            self.p.append(self.p[-1]*num)
        
        
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k>len(self.l):
                return 0
        return self.p[-1]//self.p[-(k+1)]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)