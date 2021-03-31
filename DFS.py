def maxRegion(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    maxRegion = 0
    for i in range(n):
        for j in range(m):
            if (not visited[i][j]) and grid[i][j] == 1:
                queue = [[i, j]]
                visited[i][j] = True
                count = 1
                while queue:
                    posX, posY = queue.pop()
                    moves = goodMoves(grid, posX, posY)
                    for move in moves:
                        if not visited[move[0]][move[1]]:
                            queue.append(move)
                            visited[move[0]][move[1]] = True
                            count += 1
                if maxRegion < count:
                    maxRegion = count
    return maxRegion


# Find the next move from a current position grid[i][j]
def goodMoves(grid, i, j):
    moves = list()
    n, m = len(grid), len(grid[0])
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if not (x == i and y == j):
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                    moves.append([x, y])
    return moves


# HackerRank DFS: Connected Cell in a Grid
# @para n, m: size of the grid (each element is either 0 or 1)
# @1's cells are connected to each other horizontally, vertically, or diagonally
# TODO: find the maximum area of connected cells
def main():
    n = int(input())
    m = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))
    print(maxRegion(grid))


main()