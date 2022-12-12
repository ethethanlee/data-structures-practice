# def dfs(self, i, j, matrix, visited, m, n):
#   if visited: 
#     # return or return a value
#   for dir in self.directions:
#     x, y = i + direction[0], j + direction[1]
#         if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j] (or a condition you want to skip this round):
#            continue
#         # do something like
#         visited[i][j] = True
#         # explore the next level like
#         self.dfs(x, y, matrix, visited, m, n)