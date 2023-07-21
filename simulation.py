import random
#Don't change anything except "first_guess" variable
wins = 0
first_guess = 16 #Add the first guess

for r in range(0, 100000):
    tries = 5
    number = random.randint(1, 100)
    guess = 0
    check = "high"
    while tries > 0:
        if tries == 5:
            l = 0
            h = 100
            answer = first_guess

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
print(f"The success rate for number {first_guess} as first answer is {round(0.001*wins)}%")
