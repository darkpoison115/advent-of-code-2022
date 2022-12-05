import re

filename = "input"


def remove_new_lines(lines):
    return list(map(lambda line: line[:-1], lines))


with open(filename, "r") as file:
    lines = remove_new_lines(file.readlines())
    n = lines.index("")
    number_stacks = int(lines[n - 1].strip().split(" ")[-1])

    stacks = [[] for _ in range(number_stacks)]

    last_line = lines[n - 2]
    indexes = [(i + 1) for i, char in enumerate(last_line) if char == "["]

    for line in reversed(lines[: n - 1]):
        for i, index in enumerate(indexes):
            char = line[index]
            if char != " ":
                stacks[i].append(char)

    for line in lines[n + 1 :]:
        left, right = line.split(" from ")
        quantity = int(left.split(" ")[-1])
        left, right = right.split(" to ")
        i = int(left) - 1
        j = int(right) - 1
        to_move = stacks[i][-quantity:]
        stacks[i] = stacks[i][:-quantity]
        stacks[j].extend(reversed(to_move))

    chars = [stack[-1] for stack in stacks]
    print("".join(chars))
