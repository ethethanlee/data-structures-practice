class Solution:
    def maxAreaOfIsland(self, grid):
        visited=set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        