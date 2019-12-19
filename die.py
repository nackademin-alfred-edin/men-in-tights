import random


#Casting die function, taking attribute integer value as argument
def die(attribute):
    sum = 0
    for each in range(attribute):
        sum += random.randint(1, 6)
    return sum