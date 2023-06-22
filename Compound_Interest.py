'''Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.'''

user_input=int(input("Enter the initial amount: "))

# rate_of_interest=4%
# number_of_years=3
Amount_first_year=(user_input*0.04)+user_input
rate_01=(user_input*0.04)

Amount_second_year=(Amount_first_year*0.04)+Amount_first_year
rate_02=rate_01*0.04

Amount_of_third_year=0.04*Amount_second_year+Amount_second_year
rate_03=rate_02*0.04


print(f"First year amount: {Amount_first_year:.2f} \n and the amount of amount second year: {Amount_second_year:.2f} \n Amount of third year: {Amount_of_third_year:.2f}")

# Amount=p(1+r/100) power n



