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

        


        

        dp=[0]*(amount+1)

        def sort(coins):
            for i in range(n):
                for j in range(n-i-1):
                    if coins[j]>coins[j+1]:
                        temp=coins[j]
                        coins[j]=coins[j+1]
                        coins[j+1]=temp
            return coins
            
        sort(coins)

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
    



        