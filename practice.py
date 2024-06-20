# Get the input from the user
user_input = input("Enter your age: ")

# Check if the input is a digit
if user_input.isdigit():
    # Convert the input to an integer
    convert_to_integer = int(user_input)

    # Determine the age category using if-elif-else statements
    if convert_to_integer <= 2:
        print("You are an infant")
    elif 3 <= convert_to_integer <= 12:
        print("You are a child")
    elif 13 <= convert_to_integer <= 19:
        print("You are a Teenager")
    elif 20 <= convert_to_integer <= 65:
        print("You are an Adult")
    else:
        print("You are a Senior Citizen")

    # Print the age
    print(f"You are {convert_to_integer} years old")
else:
    print("Enter the age in number: ")


