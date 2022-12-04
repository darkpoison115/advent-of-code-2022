filename = "input"

total = 0
for line in open(filename, "r"):
    left, right = line.split(",")
    a, b = map(int, left.split("-"))
    c, d = map(int, right.split("-"))
    total += ((a <= c <= b) and (a <= d <= b)) or ((c <= a <= d) and (c <= b <= d))

print(total)
