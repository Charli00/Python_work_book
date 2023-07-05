'''Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.'''

user_input=int(input("Enter the money in cents: "))


pennies = 100
nickels=120
dimes=125
quarters =300
loonies=345

tonnies=1234

if user_input >= 100:
    pennies = user_input//pennies
    print("pennies",pennies)
    user_input%pennies
if user_input >= 120:
    nickels=user_input//nickels
    print("nickels",nickels)
    user_input%nickels
if user_input >= 125:
    dimes =user_input//nickels
    print("dimes",dimes)
    user_input%dimes
if user_input>=300:
    quarters=user_input//quarters
    print("quarters",quarters)
    user_input%quarters
if user_input>=loonies:
    loonies=user_input//loonies
    print("loonies",loonies)
    user_input%loonies
if user_input>=tonnies:
    tonnies=user_input/tonnies
    print("tonnies",tonnies)
    user_input%tonnies


if user_input < 100:
    print("All the product values greater than 100")