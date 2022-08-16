class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1, p2, output = 0, len(height)-1, 0
        while p1 < p2:
            if height[p1] >= height[p2]:
                output = max(output, height[p2]*(p2-p1))
                p2-=1
            else:
                output = max(output, height[p1]*(p2-p1))
                p1+=1
        return output

    def maxAreaSlow(self, height):
        p1, p2, output = 0, len(height)-1, 0
        while p1 < p2:
            water = min(height[p1]*(p2-p1), height[p2]*(p2-p1))
            output = max(output, water)
            if height[p1] >= height[p2]:
                p2-=1
            else:
                p1+=1
        return output
sol = Solution()
print(sol.maxArea([1,2,3,4,3,2,1]))
# print(sol.maxArea([1,8,6,2,5,4,8,3,7]))