'''
    author: Mr Wright
    date: 18/08/25
    version:1
    description: Testing and commenting 
'''

import random   #get a random number, use randint,shuffle,choice
import string  #get the ascii alphabet

#---------------------------------------
# to print out a list of names
# It's takes one parameter, no return
#---------------------------------------
def display_names(names):
    
    for i in names:
        print(i, end=' ')

#---------------------------------------------
# This function takes a list of integers
# and it adds them all together into a total
# and return the total number of ages.
#---------------------------------------------
def add_ages(ages):  #takes a list as a parameter
    total_ages = 0  #this will store all the ages total
    for i in ages:
        total_ages += i
    return total_ages

names = []
ages = []
num = 0

#this loop gets ten names and ages entered
while(num < 3):
    while(True):
        try:
            name = input('Enter your name: ')
            if(len(name) >= 2 and len(name) <= 10): #test boundaries
                if(name == ' ' or name == None or name.isalpha()): #is a number or letter
                    break
            else:
                print('You did not enter a valid name length ')
        except:
            print('The input you entered was incorrect try again')
    while(True):
        try:
            age = int(input('Enter your age'))  #greater than 1 and less 130
            if(age >= 1 and age <= 130): #checking boundaries for merit
                if(not age == ' ' or not age == NONE or not age.isalpha() or not age.isdecimal()):  #checking invalids for excellence
                    break
                else:
                    print('You entered an invalid age')
            else:
                print("Your age was not in the valid range 1-130")
        except:
            print('Error occurred when entering the age.')
            
    names.append(name)
    ages.append(age)
    num += 1 #to stop it looping after 3 entries.

display_names(names)
print('Total ages is', add_ages(ages)) #added this line of code