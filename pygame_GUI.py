## Import 
import pygame

def main():
    ## Initialize pygame
    pygame.init()

    ## Create the screen
    screen = pygame.display.set_mode((800,600))

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
        screen.fill((160, 202, 217))

        ## Update display
        pygame.display.update()

## Call main function
main()