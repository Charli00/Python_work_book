import random, os, time


def dicerolls(side):
  result = random.randint(1, side)
  return result








def health():
  healthstats=((dicerolls(6) * dicerolls(12))/2)+10
  return healthstats


def strength():
  strength_stats=((dicerolls(6) * dicerolls(12))/2 )+ 12
  return strength_stats


while True:
  print("Character Builder")
  print()
  name = input("Name your Legend: ")
  print()
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  print()
  print(name)
  print(type)
  print("Health: ", health())
  print("STRENGTH: ", strength())
  print()
  playagain=input("Do you want to play again? ")
  if playagain=='NO' or 'no':
    break
time.sleep(1)
os.system('clear')

