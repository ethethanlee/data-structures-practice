class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            look = int(round((low+high)/2))
            print(look)
            if nums[look] > nums[low]:
                if target > nums[look]:
                    low = look + 1
                elif target < nums[look]:
                    if target >= nums[low]:
                        high = look - 1
                    else:
                        low = look + 1
                elif target == nums[look]:
                    return look
            elif nums[look] < nums[low]:
                if target > nums[look]:
                    if target >= nums[low]:
                        high = look - 1
                    elif target < nums[low]:
                        low = look + 1
                elif target < nums[look]:
                    high = look - 1
                else:
                    return look
            else:
                if nums[low] == target:
                    return low
                elif nums[high] == target:
                    return high
                else:
                    break
            if low == high:
                if nums[low] == target:
                    return low
                else:
                    return -1
        return -1

sol = Solution()
print(sol.search(nums = [1,3], target = 3))