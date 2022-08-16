class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pointer1 = 0
        pointer2 = len(height)-1
        return self.helper(height,pointer1,pointer2)
        
    
    def helper(self, height, p1, p2):
        if p1>p2:
            return 0
        out = min(height[p1]*(p2-p1),height[p2]*(p2-p1))
        return max(out, self.helper(height,p1+1,p2), self.helper(height,p1,p2-1))

sol = Solution()
print(sol.maxArea([1,2,3,4,3,2,1]))
# print(sol.maxArea([1,8,6,2,5,4,8,3,7]))