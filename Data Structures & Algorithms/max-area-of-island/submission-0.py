class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # keep set of visited squares
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # bounds check
            if not (0 <= r < rows and 0 <= c < cols):
                return 0
            elif grid[r][c] == 0:
                return 0
            elif (r, c) in visited:
                return 0
            
            visited.add((r, c))
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
            
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = dfs(i, j)
                    if area > maxArea:
                        maxArea = area
        
        return maxArea