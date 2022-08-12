class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for line in matrix:
            i = 0
            while i < len(matrix):
                matrix[i].insert(len(matrix), line[i])
                i+=1
        for line in matrix:
            i = 0
            while i < len(matrix):
                line.pop(0)
                i+=1

    def betterrotate(self, matrix):
        self.transpose(matrix)
        self.reflect(matrix)
        return matrix
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


                

sol = Solution()
print(sol.betterrotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))