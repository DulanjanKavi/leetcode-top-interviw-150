class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        right,left,up,down = 1,2,3,4

        total_items = len(matrix) * len(matrix[0])
        answer = []
        direction = right
        i,j =0,0

        max_i = len(matrix)-1
        min_i= 0
        max_j = len(matrix[0])-1
        min_j = 0


        while len(answer)<total_items:
            
            if direction == right:
                i = min_i
                j= min_j
                while j<=max_j:
                    answer.append(matrix[i][j])
                    j +=1
                min_i +=1
                direction = down
                

            elif direction == down:
                i= min_i
                j= max_j
                while i<=max_i:
                    answer.append(matrix[i][j])
                    i +=1
                max_j -=1
                direction = left
               

            elif direction == left:
                i= max_i
                j= max_j
                while j>=min_j:
                    answer.append(matrix[i][j])
                    j -=1
                max_i -=1
                direction = up
                

            elif direction ==up:
                i= max_i
                j= min_j
                while i>=min_i:
                    answer.append(matrix[i][j])
                    i -=1
                min_j +=1
                direction = right
                



        return answer

#Time complexity: O(n*m)
#Space complexity: (n*m)


        
