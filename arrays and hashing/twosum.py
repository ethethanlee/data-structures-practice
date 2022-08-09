from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hasher = defaultdict(int)
        hasher[(target-nums[0])] += 0
        i = 1
        while i < len(nums):
            if nums[i] in hasher:
                return[hasher[nums[i]], i]
            else:
                hasher[(target-nums[i])] += i
            i+=1

sol = Solution()
print(sol.twoSum(nums = [0,3,2,7,11,15], target = 9))