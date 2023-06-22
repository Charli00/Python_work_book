'''Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum =
(n)(n + 1)/2'''


user_input=int(input("Enter the positive interger n: "))

result=(user_input*(user_input+1))/2

print(f"The sum of first n positive integers {result}")