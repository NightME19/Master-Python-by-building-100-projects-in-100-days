import random

choice = ["Rock", "Paper", "Scissors"]

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
program_ran = random.choice(choice)

user_choice_select = choice[user_input]

print("Computer chose: {}".format(program_ran))

if (user_choice_select == program_ran):
    print("You draw")
elif (user_choice_select == choice[0]) and (program_ran == choice[2]):
    print("You win")
elif (user_choice_select == choice[1]) and (program_ran == choice[0]):
    print("You win")
elif (user_choice_select == choice[2]) and (program_ran == choice[1]):
    print("You win")
else:
    print("You lose")