class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        other = []
        for i in range(len(nums)+1):
            other.append(i)
        return (set(nums) ^ set(other)).pop()
        

sol = Solution()
print(sol.missingNumber(nums = [3,0,1]))