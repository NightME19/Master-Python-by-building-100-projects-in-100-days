import random

ran_num = random.randint(1, 100)
attempts_number = 10
easy_mode = True

print("Welcome to the Number Gruessing Game!")
print("I'm thinking of the number between 1 to 100.")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")


if mode == 'hard':
    attempts_number = 5
    easy_mode = False

for i in range(attempts_number):
    print("You have {} attempts remaining to guess the number.".format(attempts_number-i))
    in_num = int(input("Make a gruess: "))

    if in_num == ran_num:
        print("You got it! The answer was {}.".format(ran_num))
        break

    if easy_mode:
        if in_num > ran_num:
            print("Too high.")
        else:
            print("Too low.")

    print("Guess again")
else:
    print("You've run out of gruesses, you lose.")
