def get_pizza_bill_by_size(size):
    match size:
        case 'S':
            return 15
        case 'M':
            return 20
        case 'L':
            return 25


print("Welcome to the python pizza deliveries!")
size=input("What size of pizza do you want? S, M or L: ")
pepperoni=input("Do you want extra pepperoni on your pizza? Y or N: ")
extra_cheese=input("Do you want extra cheese? Y or N: ")
bill=get_pizza_bill_by_size(size)

if(pepperoni=='Y' and size=='S'):
    bill+=2
elif((pepperoni=='Y' and size=='M') or (pepperoni=='Y' and size=='L')):
    bill+=3

if(extra_cheese=='Y'):
    bill+=1

print(f"Your final bill for pizza is: ${bill}")






