# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

user_input_01=float(input("Enter the length of the room: "))

user_input_02=float(input("Enter the breadth of the room: "))

meter=3.28 #feet

# one feet = 0.3048m

feet = 0.3048

result=user_input_01*user_input_02


print(f"Area of room in meter: {user_input_01*user_input_02:.3f}")


print(f"Area of room in feet : {result*3.28:.3f}")


