class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            look = int(round((low+high)/2))
            if nums[look] == target:
                return look
            elif nums[look] > target:
                high = look-1
            elif nums[look] < target:
                low = look + 1
        return -1

sol = Solution()
print (sol.search(nums = [-1,0,3,5,9,12], target = 9))