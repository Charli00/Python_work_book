# Exercise 16: Area and Volume

# Write a program that begins by reading a radius, r , from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r . Use the pi constant in the math module in your
# calculations.

from math import pi

user_input=int(input("Enter the radius: "))

print(f"Area of a circle: {pi*(user_input**2)} and the volume of sphere : {(4/3)*pi*(user_input**3)}")
