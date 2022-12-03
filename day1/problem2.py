FILENAME = 'input.txt'

file = open(FILENAME, 'r')

calories = 0
greatests = [0, 0, 0]
for line in file:
    if line == '\n':
        for i, value in enumerate(greatests):
            if value < calories:
                greatests[i] = calories
                break
        greatests.sort()
        calories = 0
    else:
        calories += int(line[:-1])

print(sum(greatests))
