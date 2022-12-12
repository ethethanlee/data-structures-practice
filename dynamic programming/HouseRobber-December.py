class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_money = nums[-2:]
        for num in reversed(nums[0:len(nums)-2]):
            total_money.insert(0, num+max(total_money[1:]))
        return max(total_money)