import random

# Variable that will toggle whether user want to play new game after winning or loosing the game
do_you_want_to_do_you_want_to_continue = True

while do_you_want_to_do_you_want_to_continue:
    # This variable will hold the difficulty level
    difficulty_level = ""

    # This variable will hold the number of lives that should be given to user
    no_of_lives = 0

    # This variable will hold the random number
    rand = random.randint(1, 100)
    print(rand)
    def difficultyLevel():
        global difficulty_level
        global no_of_lives
        difficulty_level = input("Enter 'easy' for low level and 'hard' for high level").lower()

        if difficulty_level == 'easy':
            # Chances of lives will be 10
            no_of_lives = 10
        elif difficulty_level == 'hard':
            # Chances of lives will be 5
            no_of_lives = 5
        else:
            # User had entered invalid choice
            print("Please enter the valid choice\n")
            difficultyLevel()

    difficultyLevel()

    # Function that will contain the actual game
    def guessGame(lives):
        global do_you_want_to_do_you_want_to_continue
        # Variable indicating whether user has won the game or not
        isWon = 0
        for i in range(lives):
            user_guess = int(input("Please enter the number"))
            if(user_guess == rand):
                print("YOU WON!")
                print("Your guess was right\n")
                isWon = 1
                break
            elif user_guess > rand:
                print("The number imagined by you is higher than the randomly generated number\n")

            else:
                print("The number imagined by you is lower than the randomly generated number\n")

        if not isWon:
            print("YOU LOSE!\n")
            print(f"The number generated was {rand} \n")
            decide_new_game()
        else:
            decide_new_game()

    # Function that will set the variable do_you_want_to_do_you_want_to_continue
    def decide_new_game():
        global do_you_want_to_do_you_want_to_continue
        user_choice = input("Please enter 'y' if you want to play again or enter 'n'").lower()
        if user_choice == 'y':
            # user want to do_you_want_to_do_you_want_to_continue
            do_you_want_to_do_you_want_to_continue = True
        elif user_choice == 'n':
            # User dont want to do_you_want_to_do_you_want_to_continue
            do_you_want_to_do_you_want_to_continue = False
        else:
            print("Please enter valid choice")
            decide_new_game()

    guessGame(no_of_lives)

