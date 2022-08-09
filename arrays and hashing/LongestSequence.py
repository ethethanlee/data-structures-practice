class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        temp = 1
        values = set(nums)
        for val in nums:
            if val-1 not in values:
                while val + 1 in values:
                    temp += 1
                    val += 1
                if temp > output:
                    output = temp
            temp = 1
        return output


sol = Solution()
print(sol.longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7]))