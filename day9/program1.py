filename = "input"

directionToVec = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def update_head(head_pos, direction):
    i, j = directionToVec[direction]
    x, y = head_pos
    return (x + i, y + j)


def update_tail(head_pos, tail_pos, direction):
    i, j = head_pos
    n, m = tail_pos

    if direction in {"R", "L"} and j == m and abs(i - n) == 2:
        sign = 1 if direction == "R" else -1
        return (n + sign, j)

    if direction in {"U", "D"} and i == n and abs(j - m) == 2:
        sign = 1 if direction == "U" else -1
        return (i, m + sign)

    if i != n and j != m:
        if direction == "U" and abs(j - m) == 2:
            return (i, j - 1)
        elif direction == "D" and abs(j - m) == 2:
            return (i, j + 1)
        elif direction == "R" and abs(i - n) == 2:
            return (i - 1, j)
        elif direction == "L" and abs(i - n) == 2:
            return (i + 1, j)

    return tail_pos


head_pos = (0, 0)
tail_pos = (0, 0)

visited = set()
with open(filename, "r") as file:
    for line in file:
        direction, mag = line[:-1].split(" ")
        n = int(mag)
        for _ in range(n):
            head_pos = update_head(head_pos, direction)
            tail_pos = update_tail(head_pos, tail_pos, direction)
            visited.add(tail_pos)

print(len(visited))
