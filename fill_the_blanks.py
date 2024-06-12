print("_____ AND STEADY WINS THE RACE")
count = 0
exit = ''
print('')
print("A. SLOW")
print('')
print("B. FAST")
print('')
print("C. SLOWER")
print('')
print("D. FASTER")
print('')
print("E. SLOWLY")
print('')
print("F. FASTLY")
print('')
print("G. SLOWLY")

# user_input = input('Enter your answer: ')

# Answer = user_input
# if Answer!= 'SLOW' or Answer=='SLOW':
#         while Answer != 'SLOW':
#             count = count + 1
#             Answer = input('Incorrect.\n Try again:')
#             if Answer == 'SLOW':
#                 print('You are correct')
#                 print('')
#                 print(f'You have answered correctly after {count} attempts.')
#                 exit = input('Do you want to exit (yes or no).')
#                 if exit == 'no':
#                      continue
print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")