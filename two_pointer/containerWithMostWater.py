from collections import defaultdict


left = 0
right = 0
class Solution(object):
    def moveParam(self, height, left, right):
        left = left
        right = right
        my_dict = defaultdict(int)
        if left<right:
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -=1
            elif height[left] == height[right]:
                if height[left + 1] < height[right-1]:
                    right-=1
                    
                elif height[left + 1] > height[right-1]:
                    left += 1
                   
                else:
                    my_dict[height[right]] += (right-left)*height[right]
                    print(my_dict)
                    return self.moveParam(height, left + 1, right - 1) #return max of all of them ??
            
            return(left, right)
        else:
            bruh = max(my_dict, key=my_dict.get)
            return (bruh, bruh)

                

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        output = 0
        while left < right:
            if height[left]>height[right]:
                temp = height[right]*(right-left)
            else:
                temp = height[left]*(right-left)
            if output < temp:
                output = temp
            (left, right) = self.moveParam(height, left, right)
        return output

sol = Solution()
print(sol.maxArea([1,2,3,4,3,2,1]))
