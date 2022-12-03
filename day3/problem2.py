filename = "input"

total = 0
file = open(filename, "r")
lines = list(map(lambda line: line[:-1], file.readlines()))
groups = [lines[i : i + 3] for i in range(0, len(lines), 3)]

for group in groups:
    common = set(group[0])
    for line in group[1:]:
        common = common & set(line)

    if len(common) != 1:
        raise ValueError("Backpacks cotains more than 2 equal items.")

    element = common.pop()

    if element.islower():
        total += ord(element) - ord("a") + 1
    else:
        total += ord(element) - ord("A") + 27

print(total)
