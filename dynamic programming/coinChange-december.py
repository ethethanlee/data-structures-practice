class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = []
        dp.append(0)
        for i in range(1,amount+1):
            temp = float('inf')
            for coin in coins:
                if coin <= i:
                    temp = min(temp, 1+dp[i-coin])
            dp.append(temp)
        output = dp.pop(-1)
        if output == float('inf'):
            return -1
        return output