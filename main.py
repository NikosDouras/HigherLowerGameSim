import random

wins = 0

for r in range(0, 100000):
    tries = 5
    number = random.randint(1, 100)
    guess = 0
    check = "high"
    while tries > 0:
        if tries == 5:
            l = 0
            h = 100
            answer = 50

        else:
            if check == "high":
                h = answer
                answer = round(answer - (answer - l) / 2)
            else:
                l = answer
                answer = round(answer + (h - answer) / 2)
        tries -= 1
        if answer == number:
            tries = 0
            wins += 1
        elif answer < number:
            check = "low"
        else:
            check = "high"
print(wins)
