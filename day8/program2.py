filename = "input"


def show_grid(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print()


def viewing_distance(tree, direction):
    distance = 0

    for element in direction:
        distance += 1
        if tree <= element:
            break

    return distance


def scenic_score(tree, i, j, row, column):
    left = row[:j]
    left.reverse()
    right = row[j + 1 :]
    up = column[:i]
    up.reverse()
    down = column[i + 1 :]
    directions = [left, right, up, down]

    score = 1
    for direction in directions:
        score *= viewing_distance(tree, direction)

    return score


with open(filename, "r") as file:
    grid = []
    for line in file:
        row = list(map(int, line[:-1]))
        grid.append(row)

    best = 0
    N = len(grid)
    for i, row in enumerate(grid):
        for j, tree in enumerate(row):
            column = [grid[k][j] for k in range(N)]
            best = max(best, scenic_score(tree, i, j, row, column))
    print(best)
