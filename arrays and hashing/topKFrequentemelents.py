from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        kdict = defaultdict(int)
        i = 0
        n = 1
        while i < len(nums):
            kdict[nums[i]] += 1
            i += 1
        while len(kdict) > k:
            kdict = {key:val for key, val in kdict.items() if val != n}
            n+=1
        return (list(kdict.keys()))


sol = Solution()
print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))