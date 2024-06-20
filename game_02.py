import random, os, time


def dicerolls(side):
  result = random.randint(1, side)
  return result


def health():
  healthstats = ((dicerolls(6) * dicerolls(12)) / 2) + 10
  return healthstats


def strength():
  strength_stats = ((dicerolls(6) * dicerolls(12)) / 2) + 12
  return strength_stats


print("Character Builder")
print()
name_c1 = input("Name your Legend: ")
print()
type_c1 = input("Character Type (Human, Elf, Wizard, Orc): ")
print()
print(name_c1)
print(type_c1)
c1Health = health()
print("Health: ", c1Health)
c1strenth = strength()

print("STRENGTH: ", c1strenth)
print()

print("Who are they battling?")
name_c2 = input("Name your Legend: ")
type_C2 = input('Character Type (Human, Elf, Wizard, Orc): ')
print(name_c2)
print()
print(type_C2)
print()
c2health = health()
print("Health: ", c2health)
print()
c2strenth = strength()
print('STRENGTH: ', c2strenth)

print()

ROUND = 1
winner = None
while True:
  time.sleep(1)
  os.system("clear")
  print("BATTLE TIME")
  print()
  print("The battle begins!")
  c1Dice = dicerolls(6)
  c2Dice = dicerolls(6)
  difference = abs(c1strenth - c2strenth) + 1
  if c1Dice > c2Dice:
    c2health -= difference
    if ROUND == 1:
      print(name_c1, "wins the first blow")
    else:
      print(name_c1, "wins round", ROUND)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if ROUND == 1:
      print(name_c2, "wins the first blow")
    else:
      print(name_c2, "wins round", ROUND)
  print()
  print(name_c1)
  print("HEALTH: ", c1Health)
  print()
  print(name_c2)
  print('HEATLH: ', c2health)
  print()
  if c1Health <= 0:
    print(name_c1, "has died!")
    winner = name_c2
    break
  elif c2health <= 0:
    print(name_c2, "has died!")
    winner = name_c1
    break
  else:
    print("And they're both standing for the next round")
    ROUND += 1

time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", ROUND, "rounds")
