
class Solution:
    def threeSum(self, nums):
        output = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            pointer1 = i + 1
            pointer2 = len(nums) - 1
            while pointer1<pointer2:
                if nums[i] + nums[pointer1] + nums[pointer2] == 0:
                    if [nums[i], nums[pointer1],nums[pointer2]] not in output:
                        output.append([nums[i], nums[pointer1],nums[pointer2]])
                    pointer1+=1
                    pointer2-=1
                    while nums[pointer1] == nums[pointer1-1] and pointer1<pointer2:
                        pointer1 +=1
                    while nums[pointer2] == nums[pointer2+1] and pointer1<pointer2:
                        pointer2 -=1
                elif nums[i] + nums[pointer1] + nums[pointer2] > 0:
                    pointer2-=1
                elif nums[i] + nums[pointer1] + nums[pointer2] < 0:
                    pointer1+=1
            i+=1
        return output
sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))