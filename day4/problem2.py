filename = "input"

total = 0
for line in open(filename, "r"):
    left, right = line.split(",")
    a, b = map(int, left.split("-"))
    c, d = map(int, right.split("-"))
    total += len(set(range(a, b + 1)).intersection(range(c, d + 1))) > 0

print(total)
