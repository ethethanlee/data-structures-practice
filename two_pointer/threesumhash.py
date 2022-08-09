
class Solution:
    def threeSum(self, nums):
        output = []
        for i in range(len(nums) - 1):
            myHashtable = set()
            nums[i]
            for n in range(i + 1, len(nums)):
                if (0 - nums[i] - nums[n]) in myHashtable:
                    temp = [nums[i], 0 - nums[i] - nums[n], nums[n]]
                    temp.sort()
                    if temp not in output:
                        output.append(temp)
                myHashtable.add(nums[n])
        return output

sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums)) 