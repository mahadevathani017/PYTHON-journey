# if the bill was $150.00, split between 5 peoples,with 12% tip
#Each person should pay (150.00/5)*1.12==33.6
#round teh result to 2 decimal places=33.60
print("Welcome tip calcualator")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10,12,or 15?"))
people=int(input("Howmany people to split the bill?"))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people

# bill_with_tip=tip/100*bill+bill
# print(bill_with_tip)
print("Each person  should pay:$",round(bill_per_person,2))




