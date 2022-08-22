class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1 and nums[0] == target:
            return [0,0] 
        
        low,high=0,len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if target == nums[mid]: 
                temp = int(mid)
                while temp>0 and nums[temp-1] == nums[mid]:
                    temp-=1
                while mid<len(nums)-1 and nums[mid]==nums[mid+1]:
                    mid+=1
                return[temp,mid]
            if target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low=mid+1
        return [-1,-1]
            