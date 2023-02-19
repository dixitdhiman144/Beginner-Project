import random

def result(u,c):
    # r>s s>p p>r
    if u == 'r' and c == 's' or u == 's' and c == 'p' or u == 'p' and  c == 'r':
        return "You Win :)"
    else:
        return "You Lose :("

def play():
    user = input("Chaose a yours For 'r' for Rock, 'p' for Paper, 's' for Scissor : ")[0].lower()
    computer = random.choice(['r', 'p', 's'])
    print(f'user - {user}  computer - {computer}')

    if user == computer:
        return "Tie !"
    return result(user,computer)


print(play())