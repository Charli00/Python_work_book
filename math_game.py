# est your family and friends on their multiplication knowledge (or just be really mean to people you know and ask them to work out their multiplication tables for 5,474,000,000....)

# Prompt the user by asking for a multiplication table for the number of their choice.
# Generate the multiplication table for 1 to 10 times that number and ask each math fact as a question (psst...that's a hint).
# If the user gets the math correct, award them a point. If they get it wrong, do not give them any points.
# At the end of the 10 rounds, show the user their score out of 10 for how many math facts they got correct.
# Why not give users an emoji if they get all 10 math facts correct?
# Math Game!
# Name your multiples: 7
# 1 X 7 = 7
# Great work! 
# 2 X 7 = 14
# Awesome!
# 3 X 7 = 54
# Nope. The answer was 21. 
# ---
# You scored 3 out of 10.


print('Math game !')

user_input=int(input(("Enter the choose of mutiples table : ")))

score=0

for i in range(1,11):
    answer=int(input(f"Enter the mutiplication value {i} x {user_input}: "))
    # if answer==:
    #     print("ALert enter the value")
    if answer == i*user_input:
        score+=1
        if score==1:
            print(f'great work')
        if score==2:
            print('Awesome')
        if score==3:
            print('Well playing')
    else:
        print('Nope you enter wrong answer')
print(score)