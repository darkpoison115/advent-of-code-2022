filename = "input"

total = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

for line in open(filename, "r"):
    score = 0
    opponent, you = line[:-1].split(" ")

    choice_you = ord(you) - ord("X") + 1
    choice_opponent = ord(opponent) - ord("A") + 1

    you_win = (choice_you, choice_opponent) in [
        (ROCK, SCISSORS),
        (SCISSORS, PAPER),
        (PAPER, ROCK),
    ]

    draw = choice_you == choice_opponent
    score = you_win * 6 + draw * 3 + choice_you
    total += score

print(total)
