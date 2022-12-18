#import the random package so we can call the random.randint function
import random

#define the upper limit for the range of the guessing numbers
upper_limit=100

#invoke the random.randint(x,y) function
random_number = random.randint(1,upper_limit)

guessing = 0

#Create a loop when the user inputs a random number and return the appropriate message
while random_number != guessing:

#Ask a guessing number from the user
    guessing = int(input(f'Please guess a number from 1 to {upper_limit}: '))

#Provide feedback to the user
    if random_number > guessing:
        print('Please guess again. Your guess is too low.')
    elif random_number < guessing:
        print('Please guess again. Your guess is too high.')
        
print(f'Congrats, you guessed correct! The secret number is {random_number}.')

#Handling of the program exit
import sys
exit_program = input('Press any key to exit')
if exit_program:
    sys.exit()
