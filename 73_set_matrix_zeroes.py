class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        set_i = set()
        set_j = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==0:
                    set_i.add(i)
                    set_j.add(j) 

        
        for item in set_i:
            for j in range(n):
                matrix[item][j]=0

        for item in set_j:
            for i in range(m):
                matrix[i][item] =0

#Space complexity: O(m+n)
#Time complexity: O(m*n)
