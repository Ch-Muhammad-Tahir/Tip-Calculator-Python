# TIP CALCULATOR IN PYTHON
print("Welcome to the Tip Calculator.")
bill = float(input("What is was the total bill? $"))
tip = int(input("What percentage tip would you like to give ? 10 , 12 or 15: "))
peoples = int(input("How many people to split The Bill: "))
tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill =bill+total_tip
pre_person_bill =total_bill/peoples
finla_ammoumt = "{:.2f}".format(pre_person_bill)
print(f"Each Person Should pay ${finla_ammoumt}")
