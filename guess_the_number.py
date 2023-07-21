
import random
def level():
  print(f"you want it the easy way? (press e)\nor the hard way? (press h)")
  o = input()
  if o == "h":
    return 5
  else:
    return 10

def game(): 
  tries = level()
  number = random.randint(1,100)
  i = 0
  while tries > 0:
    
    guess = int(input(f"take a guess (1-100), you have {tries} try(s) left\n"))
    tries -=1
    if guess == number:
      tries = 0
      print("Well done!")
    elif guess < number:
      print("too low")
    else:
      print("too high")
  if guess != number:
    print("you lost")
print("The game is called 'guess the number'. It's very easy. I have a number in my mind. you have to find it. Wanna try? (y/n)")
ans = input()
while ans == "y":
  game()
  ans = input("wanna try again?")
print("\n\nok, bye")