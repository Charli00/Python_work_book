'''In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.'''

user_input_01=int(input("Enter the less number of container: "))

user_input_02=int(input("Enter the more number of containers: "))

less=0.10
more=0.25

less_value=0.10*user_input_01
more_value=0.25*user_input_02

Refund=less_value*more_value

print(f"Total refund ${Refund:.2f}.")