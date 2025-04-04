class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        if amount==0:
            return 0

        if amount<=0:
            return -1


        

        dp=[0]*(amount+1)

        coins.sort()

        for i in range(1,amount+1):
            minn=float('inf')

            for coin in coins:

                diff = i-coin
                if diff<0:
                    break
                
                minn=min(minn,dp[diff]+1)
            dp[i]=minn

        if dp[amount]< float('inf'):
            return dp[amount]
        else:
            return -1
    



        