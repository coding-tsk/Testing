
import random
import string

def display_names(names):
    for i in names:
        print(i, end=' ')

def add_ages(ages):
    total_ages = 0
    for i in ages:
        total_ages += i
    return total_ages

names = []
ages = []
num = 0

while(num <= 10):
    name = input('Enter your name: ')
    age = input('Enter your age')
    names.append(name)
    ages.append(age)

display_names(names)
add_ages(ages)