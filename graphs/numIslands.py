class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r, c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1) 
            dfs(r,c-1)
        output = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    output +=1
                    dfs(r,c)
        return output

sol = Solution()
print(sol.numIslands(grid = [["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]]))