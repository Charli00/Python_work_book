# Exercise 15: Distance Units

# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

user_input=float(input("Enter the feet in number: "))

print(f"Total number of feet in inches: {user_input*12} inches")

print(f"Total number of feet in yards: {user_input/3} yards")


# 1 miles =1760 yards=5280 feet
# 1 miles = 5280

print(f"Distance in miles: {user_input/5280} miles")