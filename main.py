import random


print("Welcome to the 'Guess the Number' game.")
print()
print("Totally Random One-to-One-Million number will be generated for you to guess.")
print()

print("Everytime you key in your response press enter. Goodluck!!!")

def showWinMessage(count):
  print("Well done! It only took you", count,"attempts.")  
  print() 
randNum = random.randint(1,1000000)
count = 0

while True:
  count+=1
  print()
  try:
    num = int(input("Guess the number. "))
    print()
  except ValueError:
    print()
    print("I am expecting positive numbers.")
    print()
    continue
  if num == randNum :
    showWinMessage(count)
    break
  elif num > randNum:
    print()
    print("too high.")
  elif num < randNum:
    print()
    print('too low.')
  elif num < 0:
    print("I don't like negative numbers. Goodbye.")
    break 


def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run to try again with a different number.""")
    print()
    continue


if __name__=="__main__":
  endGame()
  