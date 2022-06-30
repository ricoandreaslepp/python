import pygame
import random
from bisect import bisect_left

## init library
pygame.init()

## init constants
SIZE = WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SQUARE_SIZE = 50

## init window name and caption
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Path visualizer")

def grid():
    for i in range(1, WIDTH//SQUARE_SIZE-1):
        for j in range(1, HEIGHT//SQUARE_SIZE-1):
            pygame.draw.rect(win, BLACK, (SQUARE_SIZE*i, SQUARE_SIZE*j, SQUARE_SIZE, SQUARE_SIZE), 1)

def draw_sq(pos, draw_color=None, erase=False):       
    fix = 2

    rows = [SQUARE_SIZE*i for i in range(1, HEIGHT//SQUARE_SIZE)]
    cols = rows.copy()
    
    x = bisect_left(rows, pos[0])
    y = bisect_left(cols, pos[1])
    
    if erase:
        pygame.draw.rect(win, WHITE, (SQUARE_SIZE*x+fix, SQUARE_SIZE*y+fix, SQUARE_SIZE-fix*2, SQUARE_SIZE-fix*2))
    else:   
        pygame.draw.rect(win, draw_color, (SQUARE_SIZE*x+fix, SQUARE_SIZE*y+fix, SQUARE_SIZE-fix*2, SQUARE_SIZE-fix*2))
    
    print(rows, cols, x, y)

def config():
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("'r' to reset, 'x' to exit, 'c' for random color", True, (255, 0, 0), (0, 255, 0))
    textRect = text.get_rect()
    win.blit(text, textRect)
    
def main():
    win.fill(WHITE)
    config()
    
    run = True
    drawn = False
    color = RED
    i = 0

    while run:
        
        for event in pygame.event.get():
            
            # LMB
            if pygame.mouse.get_pressed()[0]:
                print("holding down", i, pygame.mouse.get_pos())
                i += 1
                
                draw_sq(pygame.mouse.get_pos(), draw_color=color)
            
            # RMB
            if pygame.mouse.get_pressed()[2]:
                draw_sq(pygame.mouse.get_pos(), erase=True)                
            
            if event.type == pygame.KEYDOWN:
                
                if pygame.key.get_pressed()[pygame.K_r]:
                    # not a good way to do it
                    main()
                    return
                
                elif pygame.key.get_pressed()[pygame.K_x]:
                    run = False
                
                elif pygame.key.get_pressed()[pygame.K_c]:
                    print("changed color")
                    color = random.choice([RED, CYAN, BLUE, YELLOW])
   
        if not drawn:
            grid()
            drawn = True
        
        pygame.display.update()

    pygame.quit()

main()
