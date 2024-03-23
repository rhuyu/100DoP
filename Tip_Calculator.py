print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")

bill = float(bill)
tip = float(tip) / 100
people = int(people)

total = round(((bill * tip) + bill) / people, 2)
print(f"Each person should pay: ${total}")