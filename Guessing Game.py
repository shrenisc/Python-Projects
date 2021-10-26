import random
highest = 10
answer = random.randint(1, highest)
number = 1
guess = int(input('Guess a number between 1 and 10 '))
if guess < answer:
    guess = int(input('Guess higher '))
    number += 1
    if guess == answer:
        print('you guessed it!'.upper())
        print(f'You took {number} tries to get the answer.')
    else:
        print(f"Sorry you haven't guessed correctly. The answer is higher than what you have guessed.")
        retry = 'y'
        while str(retry.upper()) == 'Y' or str(retry.upper()) == 'YES':
            guess = int(input('Take a guess again '))
            number += 1
            if guess < answer:
                guess = int(input('Guess higher '))
                number += 1
                if guess == answer:
                    print('you guessed it!'.upper())
                    print(f'You took {number} tries to get the answer.')
                    retry = 'n'
                else:
                    print(f"Sorry you haven't guessed correctly. The answer is higher than what you have guessed.")
                    retry = 'y'
            elif guess > answer:
                guess = int(input('Guess lower '))
                number += 1
                if guess == answer:
                    print('you guessed it!'.upper())
                    print(f'You took {number} tries to get the answer.')
                    retry = 'n'
                else:
                    print(f"Sorry you haven't guessed correctly. The answer is lower than what you have guessed.")
                    retry = 'y'
            else:
                print('you guessed it!'.upper())
                print(f'You took {number} tries to get the answer.')
                retry = 'n'
        else:
            print('Thanks for playing.')


elif guess > answer:
    guess = int(input('Guess lower '))
    number += 1
    if guess == answer:
        print('you guessed it!'.upper())
        print(f'You took {number} tries to get the answer.')

    else:
        print(f"Sorry you haven't guessed correctly. The answer is lower than what you have guessed.")
        retry = 'y'
        while str(retry.upper()) == 'Y' or str(retry.upper()) == 'YES':
            guess = int(input('Take a guess again '))
            number += 1
            if guess < answer:
                guess = int(input('Guess higher '))
                number += 1
                if guess == answer:
                    print('you guessed it!'.upper())
                    print(f'You took {number} tries to get the answer.')
                    retry = 'n'
                else:
                    print(f"Sorry you haven't guessed correctly. The answer is higher than what you have guessed.")
                    retry = 'y'
            elif guess > answer:
                guess = int(input('Guess lower '))
                number += 1
                if guess == answer:
                    print('you guessed it!'.upper())
                    print(f'You took {number} tries to get the answer.')
                    retry = 'n'
                else:
                    print(f"Sorry you haven't guessed correctly. The answer is lower than what you have guessed.")
                    retry = 'y'
            else:
                print('you guessed it!'.upper())
                print(f'You took {number} tries to get the answer.')
                retry = 'n'
        else:
            print('Thanks for playing.')
else:
    print('Congrats! You beat the game.'.upper())
    print(f'You took {number} tries to get the answer.')
