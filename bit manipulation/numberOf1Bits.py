class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        while n:
            output += n & 1
            n= n >> 1
        return output

sol = Solution()
print(sol.hammingWeight(n=20))