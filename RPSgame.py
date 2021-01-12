import random
def game(user):
    count_win = 0
    count_loss = 0
    count_tie = 0
    game_in_progress = True
    t = ['rock', 'paper', 'scissors']
    while game_in_progress == True:
        user_choice = input("Enter Rock, Paper, or Scissors: ")
        user_choice_lower = user_choice.lower()
        if user_choice_lower == 'rock':
            user_choice_to_num = 0
        elif user_choice_lower == 'paper':
            user_choice_to_num = 1
        elif user_choice_lower == 'scissors':
            user_choice_to_num = 2
        else:
            print("Wrong choice, try again!")
            continue
        # 0 = rock, 1 = paper, 2 = scissors
        computer_choice_num = random.randint(0,2)
        if (user_choice_to_num + 1) % 3 == computer_choice_num:
            count_loss += 1
            print('You lost!')

        elif user_choice_to_num == computer_choice_num:
            count_tie += 1
            print('You tied!')

        else:
            count_win += 1
            print('You won!')

        print("Wins: " + str(count_win))
        print("Losses: " + str(count_loss))

        user_answer = input("Do you want to play again[yes/no]? ")
        if user_answer.lower() == 'yes':
            continue
        game_in_progress = False
