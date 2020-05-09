## Set up a Sodoku board to be solved
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

## Function to pick an empty square
def find_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #returns the row,column of empty square


## Function to loop through numbers
## Function to find if the number is valid
## Function to print out board 
def print_board(board):
    for i in range(len(board)):
        ## Print horizontal lines after every 3rd row
        if i % 3 == 0 and i != 0 :
            print("------------------------")
        ## Iterate through each value in a row 
        for j in range(len(board[0])):
            ## print vertical lines after every 3rd column
            if j % 3 == 0 and j!=0:
                print(" | ", end = "") #print but don't go to the next line
            ## if it is the last number in the row allow to print on the next line
            if j == 8:
                print(board[i][j])
            else: 
                print(str(board[i][j])+" ",end = "")
print_board(board)

