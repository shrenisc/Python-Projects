print('Please guess a number between 1 and 10')
guess = int(input())
if guess < 5:
    print('Please guess higher')
    guess = int(input())
    if guess == 5:
        print('you guessed it!'.upper())
    else:
        print("Sorry you haven't guessed correctly")
elif guess > 5:
    print('Guess lower')
    guess = int(input())
    if guess == 5:
        print('you guessed it!'.upper())
    else:
        print("Sorry you haven't guessed correctly")
else:
    print('You guessed it!'.upper())
