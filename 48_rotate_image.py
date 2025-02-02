class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        #Transpose given matrix

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        #Get reflection of matrix

        for i in range(n):
            for j in range (n//2):
                matrix[i][j] , matrix[i][n-1-j] =    matrix[i][n-1-j] ,   matrix[i][j]


#Time complexity: O(n^2)
#Space complexity: O(1) 
