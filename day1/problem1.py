FILENAME = 'input.txt'

file = open(FILENAME, 'r')

calories = 0
greatest = 0
for line in file:
    if line == '\n':
        greatest = max(greatest, calories)
        calories = 0
    else:
        calories += int(line[:-1])

print(greatest)
