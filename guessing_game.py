Declare_variable = 30000

count = 0

while True:
  count += 1
  user_input = int(input('Enter a number: '))
  if user_input<0:
    print("You lost the game ")
    exit()
  if user_input < Declare_variable:
    print("Too Low Duddy")
  elif user_input > Declare_variable:
    print("Too High Duddy")
  elif user_input == Declare_variable:
    print("You got it right ")
    print('You Won the Match')
    break
print(f"it took you {count} guesses to get it correct")
    

