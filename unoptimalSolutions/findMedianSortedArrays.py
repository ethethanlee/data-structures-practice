import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        temp = []
        length = len(nums1 + nums2)
        # print(math.ceil(length))
        i = 0
        j = 0
        
        if length % 2 == 0:
            times = (length/2) + 1
            for n in range(times):
                if len(nums1) <= i:
                    temp.append(nums2[j])
                    j = j + 1
                    continue
                if len(nums2) <= j:
                    temp.append(nums1[i])
                    i = i + 1
                    continue
                
                if nums1[i] < nums2[j]:
                    temp.append(nums1[i])
                    i = i + 1
                else:
                    temp.append(nums2[j])
                    j = j + 1
            return (float(temp[times - 2]) + float(temp[times - 1]))/2
        else:
            times = int(math.ceil(float(length)/2))
            for n in range(times):
                if len(nums1) <= i:
                    temp.append(nums2[j])
                    j = j + 1
                    continue
                if len(nums2) <= j:
                    temp.append(nums1[i])
                    i = i + 1
                    continue
                if nums1[i] < nums2[j]:
                    temp.append(nums1[i])
                    i = i + 1
                else:
                    temp.append(nums2[j])
                    j = j + 1
            return float(temp[times - 1])

        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
# 4. Median of Sorted Arrays, O(n) runtime