import random

print('-----------------------------------------------')
print('        Guess That Number Game')
print('-----------------------------------------------')
print()

the_number = random.randint(0,100)
name = input('Please enter your first name: ')
guess = -1
while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('sorry {1}, your guess of {0} was too low'.format(guess,name))
    elif guess > the_number:
        print('sorry {}, your guess of {} was to high'.format(guess,name))
    else:
        print('Excellent work {}, you won, it was {}!'.format(name,guess))

print('done')