class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        lastt, noww = 0,0
        i = 0
        if len(nums) == 1:
            return nums[0]
        while i < (len(nums)-1):
            last, now = now, max(last + nums[i], now)
            lastt, noww = noww, max(lastt + nums[i+1], noww)
            i+=1
        return max(now, noww)
        