class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        number_of_rows = len(matrix)
        number_of_colums = len(matrix[0])

        total_number_of_items= number_of_rows * number_of_colums

        left_pointer = 0
        right_pointer = total_number_of_items - 1

        while left_pointer <= right_pointer:
            middle = (left_pointer+right_pointer)//2
            middle_number = matrix[middle//number_of_colums][middle%number_of_colums]

            if target == middle_number:
                return True

            elif target < middle_number:
                right_pointer=middle- 1
            else:
                left_pointer = middle + 1

        
        return False

#Space complexity: O(1)
#Time complexity: O(lon n)

            



        
