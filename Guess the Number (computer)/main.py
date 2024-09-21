import random


def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        else:
            print('Sorry, guess again. Too high')

    print(f'Yay! You got it! You guessed the number {random_number}')

guess(10)

def is_even(number):
    return number % 2 == 0

print(is_even(12))