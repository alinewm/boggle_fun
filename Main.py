import sys, pygame
import Game as game
import Graphics as graphics
import eztext

def main():
    pygame.init()

    size = width, height = 300, 350
    # speed = [2, 2]
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255

    screen = pygame.display.set_mode(size)
    txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
    # create the pygame clock
    clock = pygame.time.Clock()

    fresh_game = game.Game()
    fresh_game.pick_letters()

    while 1: #this is a loop good for things that will keep going the same like gifs
        clock.tick(30)

        # events for txtbx
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: sys.exit()
            # if event.key == K_RETURN in event:
            #     screen.fill(0,0,0)
        # clear screen
        screen.fill(BLACK)
        graphics.draw_grid(screen)
        graphics.draw_letters(fresh_game.sample, screen)
        # update txtbx
        val = txtbx.update(events)
        if val is not None:
            if fresh_game.is_valid(val):
                fresh_game.update_score(val)
                fresh_game.update_entries(val)
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()

if __name__ == '__main__': main()




