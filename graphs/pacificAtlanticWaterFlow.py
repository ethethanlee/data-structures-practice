class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(heights), len(heights[0])
        output = 0
        visited = set()
        def dfs(r,c,h):
            if r not in range(rows) or c not in range(cols) or heights[r][c] < h or (r, c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c,heights[r][c])
            dfs(r-1,c,heights[r][c])
            dfs(r,c+1,heights[r][c])
            dfs(r,c-1,heights[r][c])
        for r in range(rows):
            for c in range(cols):
                if heights[r][c] == 5 and (r,c) not in visited:
                    output +=1
                    dfs(r,c,heights[r][c])
                    # BADSDDDDD;ALKSDJF;ALKSDJF;LKADJF ???
        return output

sol = Solution()
print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))