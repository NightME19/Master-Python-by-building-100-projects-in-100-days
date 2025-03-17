print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like the give? 10, 12, or 15?"))
total_people = int(input("How much people to split the bill?"))

each_pay = (total_bill + (tip / 100 * total_bill)) / total_people

print(f"Each persin should pay: ${round(each_pay, 2)}")
