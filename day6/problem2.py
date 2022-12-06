filename = "input"

size = 14
with open(filename, "r") as file:
    stream = file.readline()[:-1]
    N = len(stream) - size + 1
    for i in range(N):
        if len(set(stream[i : i + size])) == size:
            print(i + size)
            break
