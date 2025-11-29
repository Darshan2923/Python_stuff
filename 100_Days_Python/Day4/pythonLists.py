import random

fruits=["Cherry","Apple","Pear"]

print(fruits[0])
print(fruits[-1])

fruits.append("Mango")
fruits.extend(["Grapes","Peach","Last"])
print(fruits)
fruits.insert(1,"Jackfruit")
print(fruits)
fruits.remove("Mango")
fruits.pop()    
print(fruits)

# Russian roulette

friends=["Alice","Bob","Charlie","David","Emanuel"]
random_person=friends[random.randrange(len(friends))]
print(random_person)

random_person=random.choice(friends)
print(random_person)

# We have a error common through ages: Index out of bound errors
