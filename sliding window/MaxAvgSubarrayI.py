class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        mySum = 0.0
        mySum = sum(nums[0:k])
        output = mySum/(float(k))
        for i in range((len(nums))-k):
            mySum = mySum - nums[i] + nums[i+k]
            if output < (mySum/(float(k))):
                output = mySum/(float(k))
        return output

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))