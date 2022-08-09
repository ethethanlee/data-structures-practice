class Solution(object):

    def qsort(self, inlist):
        if inlist == []: 
            return []
        else:
            pivot = inlist[0]
            lesser = self.qsort([x for x in inlist[1:] if x < pivot])
            greater = self.qsort([x for x in inlist[1:] if x >= pivot])
            return lesser + [pivot] + greater
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = self.qsort(nums)
        output = []
        i = 0
        k = len(nums) - 1
        if nums[i] + nums[k] > 0:
            j = len(nums) - 2
            for i in range(j + 1):
                j = len(nums) - 2
                while nums[i] + nums[j] + nums[k] > 0 & i < j:
                    output.append([nums[i], nums[j], nums[k]])
                    j = j - 1
        else:
            j = 1
            for i in range:
                j = i + 1
        while i != j != k:
            
            break
            
        return [nums[i], nums[k]]


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))