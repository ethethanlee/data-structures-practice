from collections import deque


class Solution(object):
    def shortest_flight(self, flights, source, target):
        graph = {} # are there any other nodes in the list that have no connections?
        for s,d in flights:
            if s not in graph:
                graph[s] = [d]
            else:
                graph[s].append(d)
            if d not in graph:
                graph[d] = []

        dist={key:0 for key in graph} #{1:0,2:0,...}
        visited=set()
        queue = deque([source])
        visited.add(source)

        while queue:
            current = queue.popleft()
            for item in graph[current]:
                if item not in visited:
                    visited.add(item)
                    dist[item] = dist[current]+1
                    if item==target:
                        return dist[item]-1
                    queue.add(item)
        
        return -1
            



sol = Solution()
print(sol.shortest_flight([(1,3),(2,3),(1,4),(4,3),(3,2)], 1, 2))


