# Python uses Mersenne Twister for random number generation.

# Pseudo-random number generators by khan academy

#  random module in python.

import random
import my_module

random_number=random.randint(1,10)
fav_number=my_module.my_favourite_number

random_float_between_0_and_1=random.random() # Random float numbers between 0 and 1. not including 1
random_float=print(random.uniform(1,5))
print(random_float_between_0_and_1*10) # between 0 and 10
print(random_number,fav_number)

# Heads or tails program
heads_or_tails_random=int(random.random()*10)
print(heads_or_tails_random)
if(heads_or_tails_random%2==0):
    print("Heads")
else:
    print("Tails")