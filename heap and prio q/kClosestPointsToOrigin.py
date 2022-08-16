import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = []
        heap = []
        output = []
        before = 0
        index_counter = 0
        for point in points:
            distance = ((point[0])**2)+((point[1])**2)
            distances.append(distance)
        heap = list(distances)
        heapq.heapify(heap)
        while k > 0:
            temp = heapq.heappop(heap)
            if before == temp:
                output.append(points[distances.index(temp, index_counter)])
                index_counter = distances.index(temp, index_counter) + 1
            else:
                output.append(points[distances.index(temp)])
                index_counter = distances.index(temp) + 1
            before = int(temp)
            k-=1
        return output
sol = Solution()
print (sol.kClosest(points = [[6,10],[-3,3],[-2,5],[0,2]], k = 3))

# not great runtime