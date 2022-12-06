filename = "input"

with open(filename, "r") as file:
    stream = file.readline()[:-1]
    N = len(stream) - 3
    for i in range(N):
        if len(set(stream[i : i + 4])) == 4:
            print(i + 4)
            break
