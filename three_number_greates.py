# Read the problem statement on the Instructions tab and start writing code here...
#Get the input the user will enter the three input number
#find the largest number among the three input number

#print the largest number
# Taking three numbers as input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a)
print(b)
print(c)

