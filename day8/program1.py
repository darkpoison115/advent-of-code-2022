filename = "input"


def show_grid(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print()


def visible(tree, i, j, row, column, grid):
    left = row[:j]
    right = row[j + 1 :]
    up = column[:i]
    down = column[i + 1 :]
    directions = [left, right, up, down]
    for direction in directions:
        if tree > max(direction):
            return True
    return False


with open(filename, "r") as file:
    grid = []
    for line in file:
        row = list(map(int, line[:-1]))
        grid.append(row)

    count = 0
    N = len(grid)
    for i, row in enumerate(grid[1:-1]):
        for j, tree in enumerate(row[1:-1]):
            column = [grid[k][j + 1] for k in range(N)]
            count += visible(tree, i + 1, j + 1, row, column, grid)
    print(count + 2 * len(grid) + 2 * len(grid[0]) - 4)
