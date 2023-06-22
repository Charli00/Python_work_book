'''Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b6
•
1 Introduction to Programming Exercises
The quotient when a is divided by b
The remainder when a is divided by b
The result of log 10 a
The result of a b
Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.'''

from math import log10

user_input=float(input("Enter the first value: "))

user_input_01=float(input("Enter the second value: "))

print("Sum of a and b : {} ".format(user_input+user_input_01))
print('\n')
print(f"subtraction a and b : {user_input-user_input_01}")
print('\n')
print(f"a is divided by b :{user_input/user_input_01:.2f}")
print('\n')
print(f"Remainder first value % second value {user_input%user_input_01}")
print('\n')
print(f"The result of log10: {log10(user_input)}")
print('\n')
print(f"The square of first value: {user_input**user_input_01:.1f}")

