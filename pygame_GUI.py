### HEADING INFO: GLOBAL VARS all capital
## Import 
import pygame

### GLOBAL VARIABLES ###
## Screen height, width, grid size - make sure height and width are divisible by 9
WINDOW_MULTIPLIER = 5 #modify this number to change size of grid - ensures always divisible by 9
WINDOW_SIZE = 90    #always divisible by 9  
WINDOW_HEIGHT = WINDOW_SIZE*WINDOW_MULTIPLIER
WINDOW_WIDTH = WINDOW_SIZE*WINDOW_MULTIPLIER
SQUARE_SIZE = int((WINDOW_SIZE*WINDOW_MULTIPLIER)/3)
CELL_SIZE = int(SQUARE_SIZE/3)
## FPS to run the game
FPS = 10
## Set up colors as RGB tupples
MAJOR_COLOR = (0,0,0) # color of major lines
BACKGROUND = (160, 202, 217)
MINOR_COLOR = (255,255,255) # color of minor lines

### DRAW GRID FUNCTION
def drawGrid():
    
    ## Draw minor lines
    for x in range(0,WINDOW_WIDTH,CELL_SIZE):
        pygame.draw.line(DISPLAYSCREEN,MINOR_COLOR,(x,0),(x,WINDOW_HEIGHT))
    for y in range(0,WINDOW_HEIGHT,CELL_SIZE):
        pygame.draw.line(DISPLAYSCREEN,MINOR_COLOR,(0,y),(WINDOW_WIDTH,y))
    ## Draw major lines
    for x in range(0,WINDOW_WIDTH,SQUARE_SIZE):
        pygame.draw.line(DISPLAYSCREEN,MAJOR_COLOR,(x,0),(x,WINDOW_HEIGHT))
    for y in range(0,WINDOW_HEIGHT,SQUARE_SIZE):
        pygame.draw.line(DISPLAYSCREEN,MAJOR_COLOR,(0,y),(WINDOW_WIDTH,y))
    return None

### MAIN FUNCTION
def main():
    ## Global Variables
    global FPSCLOCK,DISPLAYSCREEN # clock and screen

    ## Initialize pygame and define global variables
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSCREEN = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH)) #square display

    ## Title and Icon
    pygame.display.set_caption("Sudoku")
    icon = pygame.image.load("images/sudoku_image.png")
    pygame.display.set_icon(icon)

    ## Game Loop 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ## Background color 
        DISPLAYSCREEN.fill(BACKGROUND)
        ## Call draw grid function after setting background color
        drawGrid()

        ## Update display
        pygame.display.update()
        FPSCLOCK.tick(FPS)

## Call main function
main()