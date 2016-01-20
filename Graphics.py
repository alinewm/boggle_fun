import pygame

# TO-DO: figure out what to do about color variables and font
# change position of textboox to bottom

# these actually never get initialized
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

def draw_letters(screen, sample):
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

def draw_score(screen):
    LETTER_FONT = pygame.font.SysFont("monospace", 30)
    pos = (50,270)
    label = LETTER_FONT.render('Score: ',1, (255,255,255))
    screen.blit(label, pos)

def redraw_score(screen, score):
    LETTER_FONT = pygame.font.SysFont("monospace", 30)
    pos = (200,270)
    label = LETTER_FONT.render(score,1, (255,255,255))
    screen.blit(label, pos)

def draw_timer(screen, time):
    minutes, seconds = divmod(time, 60)
    LETTER_FONT = pygame.font.SysFont("monospace", 25)
    pos = (240,0)
    label = LETTER_FONT.render("{minutes}:{seconds}".format(minutes=minutes,seconds=seconds),1, (255,255,255))
    screen.blit(label, pos)

# def draw_textbox():
#         # screen.blit(answer, (50, 350))
#         txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
#         return txtbx