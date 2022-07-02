import random
import pygame

colors = [
    (0, 0, 0),
    (0, 240, 240),
    (0, 0, 240),
    (240, 0, 160),
    (0, 240, 0),
    (160, 0, 240),
    (240, 0, 0)
]


class Figure:
    x = 0
    y = 0

    Figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # I piece
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # J piece
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # L piece
        [[1, 2, 5, 6]],  # O piece
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # S piece
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # T piece
        [[4, 5, 9, 10], [2, 6, 5, 9]]  # Z piece
    ]

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.type = random.randint(0, len(self.Figures) - 1)
        self.color = colors[self.type+1]
        self.rotation = 0

    def image(self):
        return self.Figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.Figures[self.type])


class TetrisPiece:
    height = 0
    width = 0
    field = []
    Figure = None
    state = "start"

    def __init__(self, _height, _width):
        self.height = _height
        self.width = _width
        self.field = []
        self.state = "start"

        for i in range(_height):
            new_line = []
            for j in range(_width):
                new_line.append(0)
            self.field.append(new_line)
        self.new_figure()

    def new_figure(self):
        self.Figure = Figure(3, 0)

    def go_down(self):
        self.Figure.y += 1


def draw_grid():
    global factor
    factor = 30
    GRAY = (128, 128, 128)
    for i in range(game.height):
        for j in range(game.width):
            if game.field[i][j] == 0:
                color = GRAY
                border = 1
            else:
                color = colors[game.field[i][j]]
                border = 0
            grid = pygame.Rect(170 + j * factor, factor +
                               i * factor, factor, factor)
            pygame.draw.rect(screen, color, grid, border)


def main():
    global size, screen, game
    size = 650
    clock = pygame.time.Clock()
    fps = 5
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Tetris")
    game_over = False
    game = TetrisPiece(20, 10)

    while not game_over:

        draw_grid()

        if game.state == "start":
            game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if game.Figure is not None:
            for i in range(4):
                for j in range(4):
                  p = i*4+j
                  if p in game.Figure.image():
                        grid = pygame.Rect(170 + (j + game.Figure.x) * factor, factor +
                               (i + game.Figure.y) * factor, factor, factor)
                        pygame.draw.rect(screen, game.Figure.color, grid)
        
        
        pygame.display.update()
        clock.tick(fps)
        screen.fill(color=(200, 200, 200))
        


main()
