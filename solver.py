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
## Backtracking algorithm
def solver(board):
    find = find_empty_square(board)
    if not find: # if no more empty squares are found the board is complete
        return True
    else:
        row,col = find
    for i in range (1,10): # Loop through values
       if validate(board,i,(row,col)) == True: # If valid, plug in value
           board[row][col]= i
           if solver(board): # recursively try to solve the board - calls solver function again to try the next value
               return True
           board[row][col] = 0 #reset last entered value to 0 because solution did not work 

    return False #last solution did not work 

## Function to pick an empty square
def find_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #returns the row,column of empty square
                #call try_numbers
    return None # if no squares are empty

## Function to find if the number is valid
def validate(board,num,pos):
    ## Check row
    for i in range(len(board[0])):
        if board[pos[0]][i]== num and pos[1] != i:
            return False
    ## Check column
    for i in range(len(board)):
        if board[i][pos[1]]==num and pos[0] != i:
            return False
    ## Check square
    box_x = pos[1]//3
    box_y = pos[0]//3
    
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if num == board[i][j] and (i,j) != pos:
                return False
    ## If match not found - return true
    return True


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

## Print board before solution
print("Unsolved:")
print_board(board)
## Solve the board
solver(board)
## Print board after solution
print("Solved:")
print_board(board)

