filename = 'input'

total = 0

for line in open(filename, 'r'):
    text = line[:-1]
    half = len(text) // 2
    lower = set(text[:half])
    upper = set(text[half:])
    insersection = lower & upper

    if len(insersection) != 1:
        raise ValueError("Backpacks cotains more than 2 equal items.")

    element = insersection.pop()

    if element.islower():
        total += ord(element) - ord('a') + 1
    else:
        total += ord(element) - ord('A') + 27

print(total)
