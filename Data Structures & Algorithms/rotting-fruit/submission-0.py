class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = []
        time = 0
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # rotten orange, add to queue
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:

            length = len(q)

            # start off multiple BFS
            for i in range(length):
                r, c = q.pop(0)

                for dx, dy in directions:
                    row = r + dx
                    col = c + dy
                    if (row in range(len(grid)) and col in range(len(grid[0]))):
                        if grid[row][col] == 1:
                            q.append((row, col))
                            grid[row][col] = 2
                            fresh -= 1
            
            time += 1
        
        if fresh > 0:
            return -1
        else:
            return time
