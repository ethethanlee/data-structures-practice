import math
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        output = 0
        minValue = math.inf
        for i, val in enumerate(prices):
            if minValue > val:
                minValue = val
            elif val - minValue > output:
                output = val - minValue
        return output
                
            
            



sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))