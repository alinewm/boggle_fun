import sys, pygame
import Game as game

def main():
    pygame.init()

    size = width, height = 300, 350
    speed = [2, 2]
    black = 0, 0, 0
    WHITE = 255, 255, 255

    screen = pygame.display.set_mode(size)
    txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
    # create the pygame clock
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont("monospace", 50)

    fresh_game = game.Game()

    while 1: #this is a loop good for things that will keep going the same like gifs
    clock.tick(30)

    # events for txtbx
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()
        # if event.key == K_RETURN in event:
        #     screen.fill(0,0,0)
    # clear screen
    screen.fill(black)
    fresh_game.draw_grid()
    fresh_game.draw_letters()
    # update txtbx
    val = txtbx.update(events)
    if val is not None:
        # print val
        if fresh_game.is_valid(val):
            entries.append(val)
            # print val
        # print val
    # blit txtbx on the sceen
    txtbx.draw(screen)
    # refresh the display
    pygame.display.flip()

if __name__ == '__main__': main()




