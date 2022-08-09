class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        backwards = nums[::-1]
        output = []
        prev = 1
        for val in nums:
            output.append(prev)
            prev = prev*val
        prev = 1
        for i, backVal in enumerate(backwards):
            output[len(nums) - i - 1] = output[len(nums) - i - 1] * prev
            prev = prev*backVal
        return output

    def productExceptSelfnew(self,nums):
        output = []
        prev = 1
        for val in nums:
            output.append(prev)
            prev = prev*val
        prev = 1
        for i in range(len(nums) - 1 , -1, -1):
            print(i)
            output[i] = output[i] * prev
            prev = prev*nums[i]
        return output

    def productExceptSelfnewnew(self, nums):
        output = [1] * (len(nums))
        backwards = nums[::-1]
        prev = 1
        for n in range(len(nums)):
            output[n] = output[n] * prev
            prev = prev*nums[n]
        prev = 1
        for i, backVal in enumerate(backwards):
            output[len(nums) - i - 1] = output[len(nums) - i - 1] * prev
            prev = prev*backVal
        return output

    def productExceptSelfbest(self, nums):
        ans = [1 for _ in nums]
        
        left = 1
        right = 1
        
        for i in range(len(nums)):
            ans[i] *= left
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        
        return ans

sol = Solution()
print(sol.productExceptSelfbest([1,2,3,4]))
        