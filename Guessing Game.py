print('Please guess a number between 1 and 10')
guess = int(input())
if guess < 5:
    print('Please guess higher')
    guess = int(input())
    if guess == 5:
        print('you guessed it!'.upper())
    else:
        print("Sorry you haven't guessed correctly")
        retry = input('Do you want to try again?(Y/N)')
        if str(retry.upper()) == 'Y':
            print('Coming Soon')
        elif str(retry.upper()) == 'N':
            print('Good choice')
elif guess > 5:
    print('Guess lower')
    guess = int(input())
    if guess == 5:
        print('you guessed it!'.upper())
    else:
        print("Sorry you haven't guessed correctly")
        retry = input('Do you want to try again?(Y/N)')
        if str(retry.upper()) == 'Y':
            print('Coming Soon')
        elif str(retry.upper()) == 'N':
            print('Good choice')
else:
    print('You guessed it!'.upper())
