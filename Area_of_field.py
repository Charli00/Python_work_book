# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
user_input_01=float(input("Enter the length in feet: "))

user_input_02=float(input("Enter the breadth in feet: "))

Area=user_input_01*user_input_02

print(f"{Area/43560:.3f}")