print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
#change bill value from string to float
bill_float = float(bill)
percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
#change percent value from string to float
percent_float = float(percent)
tip_bill = bill_float * percent_float / 100
#add the split bill percentage and bill
total_bill = bill_float + tip_bill

split = input("How many people to split the bill? ")
#change split from string to float
split_float= float(split)
pay = round(total_bill / split_float, 2)
message = (f"Each person should pay: ${pay}")
print(message)
