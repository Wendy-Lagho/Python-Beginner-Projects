import random

def play():
    user = input("What\'s your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors: \n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It\'s a tie!"
    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You won!"

    return "You lost!"


def is_win(player, computer):
    #return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
        or (player == 'p' and computer == 'r'):
        return True

print(play())