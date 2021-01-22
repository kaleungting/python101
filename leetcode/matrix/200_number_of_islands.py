def numIslands(self, grid: List[List[str]]) -> int:
    def flipIslands(i, j):
        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        flipIslands(i-1, j)
        flipIslands(i+1, j)
        flipIslands(i, j-1)
        flipIslands(i, j+1)

    islandCount = 0
    row, col = len(grid), len(grid[0])

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                islandCount += 1
                flipIslands(i, j)

    return islandCount
