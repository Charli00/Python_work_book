#Loan Calculator
#p=10000
#r=0.05

#n=12
# pnr/100

user_input = float(input("Enter the amount of money you want to borrow: "))
a = user_input
for i in range(11):
  # print("Year", i+1, "is", a)
  Borrowed_money = a * 0.05
  TOtal_Amount = a + Borrowed_money
  print()
  print(f"year {i} and the Total amount of interest is :{TOtal_Amount}")
  a = TOtal_Amount
