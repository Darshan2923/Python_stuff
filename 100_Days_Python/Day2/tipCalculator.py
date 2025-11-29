def tip_calculate(total_bill,tip_percentage,number_splits):
    total_bill_with_tip=total_bill+total_bill*tip_percentage/100
    each_person_pay=total_bill_with_tip/number_splits
    return round(each_person_pay,2)

print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip_percentage=int(input("How much tip would you like to give? 10, 12, or 15? "))
number_splits=int(input("How many people to split the bill? "))

per_person_split=tip_calculate(total_bill,tip_percentage,number_splits)

print(f"Each person should pay: ${per_person_split}")

