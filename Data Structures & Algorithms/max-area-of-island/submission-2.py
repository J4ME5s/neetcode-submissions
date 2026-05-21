class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return 0
            if grid[r][c] == 0:
                return 0
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        
        maxArea = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea
        
        