class Solution(object):
    def climbStairs(self, n):
        a = b = 1
        i = 0
        while n > i:
            a, b = b, a + b
            i+=1
        return a