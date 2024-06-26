def displayboard():
    print(" _______________________")
    print("|   " + board[7] + "   |   " + board[8] + "   |   " + board[9] + "   |")
    print("|_______|_______|_______|")
    print("|   " + board[4] + "   |   " + board[5] + "   |   " + board[6] + "   |")
    print("|_______|_______|_______|")
    print("|   " + board[1] + "   |   " + board[2] + "   |   " + board[3] + "   |")
    print("|_______|_______|_______|")


def inputuser():
    inp = ""
    while inp not in ["X", "O","x","o"]:
        inp = input("Enter the sign to be assigned for Player 1(X or O):")
        if inp not in ["X", "O","x","o"]:
            print("Wrong input. Try Again")
        else:
            print(inp + " assigned for Player 1")
    return inp


def playgame():
    inp = ""
    while inp not in range(0, 10):
        inp = int(
            input(
                "Enter the position on numberplate where you would like to insert your tics and tacs:"
            )
        )
        if inp not in range(0, 10):
            print("Wrong input. Try Again")
    return inp


playagain = True

while playagain == True:
    board = [" "] * 10
    board[0]=0
    x = inputuser()
    def game(x):
        if x.upper() == "X":
            y = "O"
        if x.upper() == "O":
            y = "X"
        bronte = False
        displayboard()
        while bronte == False:
            if " " not in board:
                bronte = True
                print("There's been a tie")
                break
            i = playgame()
            while(board[i]!=" "):
                print("Please Choose Again")
                i = playgame()
            board[i] = x
            displayboard()
            if board[7] == board[8] == board[9] == x:
                bronte = True
                print(x + " won")
                break
            if board[4] == board[5] == board[6] == x:
                bronte = True
                print(x + " won")
                break
            if board[1] == board[2] == board[3] == x:
                bronte = True
                print(x + " won")
                break
            if board[7] == board[4] == board[1] == x:
                bronte = True
                print(x + " won")
                break
            if board[7] == board[4] == board[1] == x:
                bronte = True
                print(x + " won")
                break
            if board[8] == board[5] == board[2] == x:
                bronte = True
                print(x + " won")
                break
            if board[9] == board[6] == board[3] == x:
                bronte = True
                print(x + " won")
                break
            if board[7] == board[5] == board[3] == x:
                bronte = True
                print(x + " won")
                break
            if board[9] == board[5] == board[1] == x:
                bronte = True
                print(x + " won")
                break
            if " " not in board:
                bronte = True
                print("There's been a tie")
                break
            i = playgame()
            while(board[i]!=" "):
                print("Please Choose Again")
                i = playgame()
            board[i] = y
            displayboard()
            if board[7] == board[8] == board[9] == y:
                bronte = True
                print(y + " won")
            if board[4] == board[5] == board[6] == y:
                bronte = True
                print(y + " won")
            if board[1] == board[2] == board[3] == y:
                bronte = True
                print(y + " won")
            if board[7] == board[4] == board[1] == y:
                bronte = True
                print(y + " won")
            if board[7] == board[4] == board[1] == y:
                bronte = True
                print(y + " won")
            if board[8] == board[5] == board[2] == y:
                bronte = True
                print(y + " won")
            if board[9] == board[6] == board[3] == y:
                bronte = True
                print(y + " won")
            if board[7] == board[5] == board[3] == y:
                bronte = True
                print(y + " won")
            if board[9] == board[5] == board[1] == y:
                bronte = True
                print(y + " won")
    game(x)            
    inp = ""
    while inp not in ["Y", "N","y","n"]:
        inp = input("Wanna Play Again?  [Y/N]")
        if inp not in ["Y", "N","y","n"]:
            print("Wrong input. Try Again")
        elif inp.upper() == "Y":
            playagain = True
        elif inp.upper() == "N":
            playagain = False
            