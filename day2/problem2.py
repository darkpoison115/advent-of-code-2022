filename = "input"

total = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

winning_strategy = [PAPER, SCISSORS, ROCK]
losing_strategy = [SCISSORS, ROCK, PAPER]

for line in open(filename, "r"):
    score = 0
    opponent, strategy = line[:-1].split(" ")
    choice_opponent = ord(opponent) - ord("A")

    draw = False
    you_win = False
    choice_you = 0
    if strategy == 'X':
        choice_you = losing_strategy[choice_opponent]

    if strategy == 'Y':
        draw = True
        choice_you = choice_opponent + 1

    if strategy == 'Z':
        you_win = True
        choice_you = winning_strategy[choice_opponent]

    score = you_win * 6 + draw * 3 + choice_you
    total += score

print(total)
