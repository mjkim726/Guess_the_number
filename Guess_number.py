import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secret_number = random.randint(1,20)

guesses = []
number_of_guesses = 6
for guess_taken in range(1, 7):
    print('Take a guess. You have ' + str(number_of_guesses) + ' guesses left.' )
    try:
        guess = int(input())
        if guess in guesses:
            print("You already guessed " + str(guess))
            number_of_guesses -= 1
        else:
            guesses.append(guess)
            if guess < secret_number:
                print("Your guess is too low.")
                number_of_guesses -= 1
            elif guess > secret_number:
                print("Your guess is too high.")
                number_of_guesses -= 1
            else:
                #correct guess
                break
    except:
        print('You need to choose an integer! Try again!')
        guess = int(input())
        if guess in guesses:
            print("You already guessed " + str(guess))
            number_of_guesses -= 1
        else:
            guesses.append(guess)
            if guess < secret_number:
                print("Your guess is too low.")
                number_of_guesses -= 1
            elif guess > secret_number:
                print("Your guess is too high.")
                number_of_guesses -= 1
            else:
                #correct guess
                break

if guess == secret_number:
    print('Good job,' + name + "! You guesssed my number in " + str(guess_taken) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number) + '.')
