guess = int(input('Guess a number between 1 and 10 '))
if guess < 5:
    guess = int(input('Guess higher '))
    if guess == 5:
        print('you guessed it!'.upper())
        retry = input('Do you want to play again?(Y/N)')
        while str(retry.upper()) == 'Y':
            guess = int(input('Guess a number between 1 and 10 '))
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
                print('Congrats! You beat the game.'.upper())
                retry = 'n'
        else:
            print('Thanks for playing.')
    else:
        print("Sorry you haven't guessed correctly")
        retry = input('Do you want to play again?(Y/N)')
        while str(retry.upper()) == 'Y':
            guess = int(input('Guess a number between 1 and 10 '))
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
                print('Congrats! You beat the game.'.upper())
                retry = 'n'
        else:
            print('Thanks for playing.')


elif guess > 5:
    guess = int(input('Guess lower '))
    if guess == 5:
        print('you guessed it!'.upper())
        retry = input('Do you want to play again?(Y/N)')
        while str(retry.upper()) == 'Y':
            guess = int(input('Guess a number between 1 and 10 '))
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
                print('Congrats! You beat the game.'.upper())
                retry = 'n'
        else:
            print('Thanks for playing.')
    else:
        print("Sorry you haven't guessed correctly")
        retry = input('Do you want to play again?(Y/N)')
        while str(retry.upper()) == 'Y':
            guess = int(input('Guess a number between 1 and 10 '))
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
                print('Congrats! You beat the game.'.upper())
                retry = 'n'
        else:
            print('Thanks for playing.')
else:
    print('Congrats! You beat the game.'.upper())
