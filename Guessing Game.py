guess = int(input('Please guess a number between 1 and 10 '))
if guess < 5:
    guess = int(input('Guess higher '))
    if guess == 5:
        print('you guessed it!'.upper())
        retry = input('Do you want to play again?(Y/N)')
        while str(retry.upper()) == 'Y':
            guess = int(input('Please guess a number between 1 and 10 '))
            if guess < 5:
                guess = int(input('Guess higher '))
                if guess == 5:
                    print('you guessed it!'.upper())
                    retry = input('Do you want to play again?(Y/N)')
                else:
                    print("Sorry you haven't guessed correctly")
                    retry = input('Do you want to play again?(Y/N)')
            elif guess > 5:
                guess = int(input('Guess lower '))
                if guess == 5:
                    print('you guessed it!'.upper())
                    retry = input('Do you want to play again?(Y/N)')
                else:
                    print("Sorry you haven't guessed correctly")
                    retry = input('Do you want to play again?(Y/N)')
        else:
            print('Cool! Thanks for playing.')
    else:
        print("Sorry you haven't guessed correctly")
        retry = input('Do you want to play again?(Y/N)')
        while str(retry.upper()) == 'Y':
            guess = int(input('Please guess a number between 1 and 10 '))
            if guess < 5:
                guess = int(input('Guess higher '))
                if guess == 5:
                    print('you guessed it!'.upper())
                    retry = input('Do you want to play again?(Y/N)')
                else:
                    print("Sorry you haven't guessed correctly")
                    retry = input('Do you want to play again?(Y/N)')
            elif guess > 5:
                guess = int(input('Guess lower '))
                if guess == 5:
                    print('you guessed it!'.upper())
                    retry = input('Do you want to play again?(Y/N)')
                else:
                    print("Sorry you haven't guessed correctly")
                    retry = input('Do you want to play again?(Y/N)')
        else:
            print('Cool! Thanks for playing.')


elif guess > 5:
    guess = int(input('Guess lower '))
    if guess == 5:
        print('you guessed it!'.upper())
        retry = input('Do you want to play again?(Y/N)')
        while str(retry.upper()) == 'Y':
            guess = int(input('Please guess a number between 1 and 10 '))
            if guess < 5:
                guess = int(input('Guess higher '))
                if guess == 5:
                    print('you guessed it!'.upper())
                    retry = input('Do you want to play again?(Y/N)')
                else:
                    print("Sorry you haven't guessed correctly")
                    retry = input('Do you want to play again?(Y/N)')
            elif guess > 5:
                guess = int(input('Guess lower '))
                if guess == 5:
                    print('you guessed it!'.upper())
                    retry = input('Do you want to play again?(Y/N)')
                else:
                    print("Sorry you haven't guessed correctly")
                    retry = input('Do you want to play again?(Y/N)')
        else:
            print('Cool! Thanks for playing.')
    else:
        print("Sorry you haven't guessed correctly")
        retry = input('Do you want to play again?(Y/N)')
        while str(retry.upper()) == 'Y':
            guess = int(input('Please guess a number between 1 and 10 '))
            if guess < 5:
                guess = int(input('Guess higher '))
                if guess == 5:
                    print('you guessed it!'.upper())
                    retry = input('Do you want to play again?(Y/N)')
                else:
                    print("Sorry you haven't guessed correctly")
                    retry = input('Do you want to play again?(Y/N)')
            elif guess > 5:
                guess = int(input('Guess lower '))
                if guess == 5:
                    print('you guessed it!'.upper())
                    retry = input('Do you want to play again?(Y/N)')
                else:
                    print("Sorry you haven't guessed correctly")
                    retry = input('Do you want to play again?(Y/N)')
        else:
            print('Cool! Thanks for playing.')
else:
    print('You guessed it!'.upper())
