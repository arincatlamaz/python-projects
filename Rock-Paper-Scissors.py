print("Welcome to game Rock - Paper - Scissors")

def get_input_uzyt():
    pone = input("Player one choice : ")
    ptwo = input("Player two choice :")
    return pone,ptwo

def ext():
    line = input("Do you want to play again ? If yes write 'y' If not write 'n' :")
    if line == "n":
        return False
    elif line != "y":
        print("unknown input")
        return False

    return True

line = ext()
while(line):
    pone,ptwo = get_input_uzyt()
    if pone == "rock" and ptwo == "paper":
        print("Winner is 2. Player , Congratulations")

    elif pone == "paper" and ptwo == "rock":
        print("Winner is 1. Player Congratulations")

    if pone == "paper" and ptwo == "scissors":
        print("Winner is 2. Player , Congratulations")

    elif pone == "scissors" and ptwo == "paper":
        print("Winner is 1. Player , Congratulations")

    if pone == "rock" and ptwo == "scissors":
        print("Winner is 1. Player , Congratulations")

    elif pone == "scissors" and ptwo == "rock":
        print("Winner is 2. Player Congratulations")

    line = ext()