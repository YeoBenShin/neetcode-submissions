# class Solution:
#     from collections import deque
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # at each possible land, i.e. '1' 
#         # search out for other '1's
#         # for each of the '1's that are found
#         # repeat the search 

#         nCol = len(grid[0])
#         nRow = len(grid)

#         checked = [[-1 for _ in range(nCol)] for _ in range(nRow)] # identify what you have checked.
#         # instead of keeping track of what we have searched,
#         # we can just turn searched loc that have value == '1' and turn them to '0'

#         def searchNeig(row, col):
#             if (row - 1 >= 0):
#                 if (checked[row-1][col] == -1):
#                     checked[row-1][col] = 1
#                     if grid[row-1][col] == "1":
#                         queue.append((row-1, col))

#             if (row + 1 < nRow):
#                 if (checked[row+1][col] == -1):
#                     checked[row+1][col] = 1
#                     if grid[row+1][col] == "1":
#                         queue.append((row+1, col))

#             if (col + 1 < nCol):
#                 if (checked[row][col+1] == -1):
#                     checked[row][col+1] = 1
#                     if grid[row][col+1] == "1":
#                         queue.append((row, col+1))

#             if (col - 1 >= 0):
#                 if (checked[row][col-1] == -1):
#                     checked[row][col-1] = 1
#                     if grid[row][col-1] == "1":
#                         queue.append((row, col-1))

#         counter = 0
#         queue = deque()
#         for i in range(nRow):
#             for j in range(nCol):
#                 if (checked[i][j] == 1): # checked 
#                     continue 
#                 checked[i][j] = 1 # mark as checked
#                 if (grid[i][j] == '1'):
#                     counter += 1
#                     searchNeig(i,j)
#                 while (len(queue) != 0):
#                     r, c = queue.popleft()
#                     searchNeig(r,c)
#         return counter

# less memory usage. 
# instead of keeping track of what we have searched,
# we can just turn searched loc that have value == '1' and turn them to '0'
class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        # at each possible land, i.e. '1' 
        # search out for other '1's
        # for each of the '1's that are found
        # repeat the search 

        nCol = len(grid[0])
        nRow = len(grid)

        def searchNeig(row, col):
            if (row - 1 >= 0):
                if grid[row-1][col] == "1":
                    grid[row-1][col] = "0"
                    queue.append((row-1, col))

            if (row + 1 < nRow):
                if (grid[row+1][col] == '1'):
                    grid[row+1][col] = "0"
                    queue.append((row+1, col))

            if (col + 1 < nCol):
                if (grid[row][col+1] == '1'):
                    grid[row][col+1] = "0"
                    queue.append((row, col+1))

            if (col - 1 >= 0):
                if (grid[row][col-1] == '1'):
                    grid[row][col-1] = "0"
                    queue.append((row, col-1))

        counter = 0
        queue = deque()
        for i in range(nRow):
            for j in range(nCol):
                if (grid[i][j] == '1'):
                    counter += 1
                    grid[i][j] == '0'
                    searchNeig(i,j)
                while (len(queue) != 0):
                    r, c = queue.popleft()
                    searchNeig(r,c)
        return counter
            
 
