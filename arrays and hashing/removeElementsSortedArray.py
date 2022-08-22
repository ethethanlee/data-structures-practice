class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        count = 0
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                count+=1
            else:
                i+=1
        # while count > 0:
        #     nums.append(0)
        #     count-=1
                