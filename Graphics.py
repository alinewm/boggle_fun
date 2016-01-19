import pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255
SIZE = WIDTH, HEIGHT = 300, 350
# LETTER_FONT = pygame.font.SysFont("monospace", 50)

def draw_grid(screen):
    # vertical lines
    pygame.draw.line(screen, WHITE, (50,50), (50, 250), 2)
    pygame.draw.line(screen, WHITE, (100,50), (100, 250), 2)
    pygame.draw.line(screen, WHITE, (150,50), (150, 250), 2)
    pygame.draw.line(screen, WHITE, (200,50), (200, 250), 2)
    pygame.draw.line(screen, WHITE, (250,50), (250, 250), 2)
    # horizontal lines
    pygame.draw.line(screen, WHITE, (50,50), (250, 50), 2)
    pygame.draw.line(screen, WHITE, (50,100), (250, 100), 2)
    pygame.draw.line(screen, WHITE, (50,150), (250, 150), 2)
    pygame.draw.line(screen, WHITE, (50,200), (250, 200), 2)
    pygame.draw.line(screen, WHITE, (50,250), (250, 250), 2)

def draw_letters(sample, screen):
    LETTER_FONT = pygame.font.SysFont("monospace", 50)
    points = [(50,50), (100,50), (150, 50), (200,50), \
            (50,100), (100,100), (150,100), (200,100), \
            (50,150), (100,150), (150,150), (200,150), \
            (50, 200), (100,200), (150, 200), (200,200)]
    letter_and_pos = zip(sample, points)
    # print letter_and_pos
    for letter, pos in letter_and_pos:
        label = LETTER_FONT.render(letter, 1, (225,225,0))
        screen.blit(label, pos)