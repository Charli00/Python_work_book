'''Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.'''

user_input=float(int(input(("Enter the TOtal feet in number: "))))

user_input_01=float(input("Enter the Total iches in number: "))

total_inches=(user_input*12)+user_input_01

centimeters=total_inches*2.54

print(f"Height in centimeter: {centimeters}")
