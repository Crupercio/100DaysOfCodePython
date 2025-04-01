print("Welcome to the tip calculator!")
#Input section with clear prompts
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#Calculate total bill with tp
tip_multiplier = 1 + (tip_percentage / 100)
total_bill = bill * tip_multiplier

#Calculate per person amount

amount_per_person = round((total_bill / people), 2)


print(f"Each person should pay: ${amount_per_person:.2f}")
