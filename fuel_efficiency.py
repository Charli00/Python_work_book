user_input=float(input("Enter the MPG value: "))

kilometers_per_mile=1.609

Liter_per_gallon=3.784

#miles to kilometers

Miles_per_kilometers=user_input*kilometers_per_mile

#gallon to litres

Gallon_per_litres=Miles_per_kilometers*Liter_per_gallon

# calculate litres per kilometers
litre_pre_100km=100/Gallon_per_litres

print(litre_pre_100km)