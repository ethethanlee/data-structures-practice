import math
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        output = math.inf
        window = []
        sumWind = 0
        if sum(nums) < target:
            return 0
        while nums != []:
            print(window)
            if sumWind >= target:
                if len(window) < output:
                    output = len(window)
                sumWind = sumWind - window[0]
                window = window[1:]
            else:
                window.append(nums.pop(0))
                sumWind += nums.pop(0)
        if len(window) < output:
            output = len(window)
        while sumWind >= target:
            if len(window) < output:
                output = len(window)
            sumWind = sumWind - window[0]
            window = window[1:]
        return output

sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))