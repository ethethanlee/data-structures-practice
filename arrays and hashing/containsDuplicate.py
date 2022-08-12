class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        values = set()
        i = 0
        while i < len(nums):
            if nums[i] in values:
                return True
            else:
                values.add(nums[i])
            print(i)
            i+=1
        return False

sol = Solution()

print(sol.containsDuplicate(nums = [1,2,3,4]))