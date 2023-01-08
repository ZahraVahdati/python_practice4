#Tic Tok Toe
def show():
    for row in game_board:
        for cell in row:
            print(cell,end="")
        print()

def check_game():
    if game_board[0][0]=="x " and game_board[0][1]=="x " and  game_board [0][2]=="x ":
        print("the first player win")

    if game_board[1][0]== "x " and game_board[1][1]=="x " and game_board[1][2]=="x ":
        print("the first player win")
    
    if game_board[2][0]=="x " and game_board[2][1]=="x " and game_board[2][2]=="x ":
         print("the first player win")
    
    if game_board[0][0]=="x " and game_board[1][1]=="x " and game_board[2][2]=="x ":
         print("the first player win")
         
    if game_board[0][2]=="x " and game_board[1][1]=="x " and game_board[2][0]=="x ":
         print("the first player win") 
         
    if game_board[0][0]=="x " and game_board[1][0]=="x " and game_board[2][0]=="x ":
         print("the first player win") 
         
    if game_board[0][1]=="x " and game_board[1][1]=="x " and game_board[2][1]=="x ":
         print("the first player win") 
         
    if game_board[0][2]=="x " and game_board[1][2]=="x " and game_board[2][2]=="x ":
         print("the first player win") 




    if game_board[0][0]=="y " and game_board[0][1]=="y " and  game_board [0][2]=="y ":
        print("the second player win")

    if game_board[1][0]== "y " and game_board[1][1]=="y " and game_board[1][2]=="y ":
        print("the second player win")
    
    if game_board[2][0]=="y " and game_board[2][1]=="y " and game_board[2][2]=="y ":
         print("the second player win")
    
    if game_board[0][0]=="y " and game_board[1][1]=="y " and game_board[2][2]=="y ":
         print("the second player win")
         
    if game_board[0][2]=="y " and game_board[1][1]=="y " and game_board[2][0]=="y ":
         print("the second player win") 
         
    if game_board[0][0]=="y " and game_board[1][0]=="y " and game_board[2][0]=="y ":
         print("the second player win") 
         
    if game_board[0][1]=="y " and game_board[1][1]=="y " and game_board[2][1]=="y ":
         print("the second player win") 
         
    if game_board[0][2]=="y " and game_board[1][2]=="y " and game_board[2][2]=="y ":
         print("the second player win") 

   
    
    else:
        print("The result is equal")


game_board= [["- ","- ","- "],
             ["- ","- ","- "],
             ["- ","- ","- "]]

show()

while True:
    print("First player")
    while True:
        row=int(input())
        col=int(input())
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col]=="- ":
                game_board[row][col] = "x "
                show()
                break
            else:
                print("select another cell")
        else:
            print("enter row and col between 0 and 2")


    print("Second player")
    while True:
        row=int(input())
        col=int(input())
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col]=="- ":
                game_board[row][col] = "y "
                show()
                break
            else:
               print("select another cell")

        else:
            print("enter row and col between 0 and 2")
