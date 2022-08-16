import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        maxHeap = [item*(-1) for item in stones]
        heapq.heapify(maxHeap)
        i = 0
        while len(maxHeap) > 1:
            largest = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            newest = largest - second
            if newest != 0:
                heapq.heappush(maxHeap, newest)
        if maxHeap:
            output = heapq.heappop(maxHeap)
            output = 0 - output
        else:
            output = 0
        return output


sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))