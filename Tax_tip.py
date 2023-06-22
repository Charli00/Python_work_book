'''The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.'''

user_input=int(input("Enter the cost of a meal ordered: "))
#4/100= 0.04
local_tax=0.05*user_input
tip_for_meal_amount=0.18*user_input

grand_total=local_tax+tip_for_meal_amount+user_input

print(f"Grand Total of meals with tax and tip: {grand_total:.2f} amount")