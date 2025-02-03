class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # Create a copy of the original board
        copy_board = [[board[i][j] for j in range(n)] for i in range(m)]
        
        # Directions for the 8 neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < m and 0 <= nj < n and copy_board[ni][nj] == 1:
                        live_neighbors += 1
                
                # Apply the rules of the Game of Life
                if copy_board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 0
                if copy_board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 1

#Time complexity: O(n*m)
#Space complexity: O(n*m)


