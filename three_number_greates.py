# Read the problem statement on the Instructions tab and start writing code here...
#Get the input the user will enter the three input number
#find the largest number among the three input number

#print the largest number

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a < b or b < c:
    print(a,b,c)
elif c<a or c<b:
    print(a,c,b)
else:
    print(" n")