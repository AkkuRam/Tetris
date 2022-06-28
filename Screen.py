import pygame

def draw_grid():
    #8 x 20 grid
    square_size = 30
    for i in range(100, 320, square_size):
        for j in range(20, 610, square_size):
            grid = pygame.Rect(i + 100,j + 10,square_size,square_size)
            pygame.draw.rect(screen, (200,200,200), grid, 2)




def main():
    global size, screen
    size = 650

    screen = pygame.display.set_mode((size, size))

    game_over = False

    while not game_over:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            

        pygame.display.update()



main()
