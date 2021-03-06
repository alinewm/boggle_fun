import sys, pygame
import random
import eztext
import numpy as np
import BoggleSolver as bs

# now that we have the solutions generator, we have to store the typed answers somewhere
# and check the typed up answer if it's valid
# also, make scores rule and tracker
# show cumulative score
 
def main():
    pygame.init()

    size = width, height = 300, 350
    speed = [2, 2]
    black = 0, 0, 0
    WHITE = 255, 255, 255

    answers = []
    entries = []
    score = []

    screen = pygame.display.set_mode(size)
    txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
    # create the pygame clock
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont("monospace", 50)
    # sample = pick_letters()

    def pick_letters():
        alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        sample = random.sample(alphabet, 16)
        # sample = np.array(random.sample(alphabet, 16)) # numpy or not?
        # matrix = np.reshape(sample, (-1, 4)) #(-1, ncolumns)
        # for number in sample:
        # using nested lists makes zipping harder
        # points = [[(50,50), (100,50), (150, 50), (200,50)], \
        #             [(50,100), (100,100), (150,100), (200,100)], \
        #             [(50,150), (100,150), (150,150), (200,150)], \
        #             [(50, 200), (100,200), (150, 200), (200,200)]]
        # points = [(50,50), (100,50), (150, 50), (200,50), \
        #             (50,100), (100,100), (150,100), (200,100), \
        #             (50,150), (100,150), (150,150), (200,150), \
        #             (50, 200), (100,200), (150, 200), (200,200)]
        # letter_and_pos = zip(sample, points)

        # solver = bs.BoggleSolver(sample)
        # answers = [word[0] for word in solver.solve()]
        # print answers
        # print type(answers[0])
        return sample
        # return sample of letters coupled with their positions

    # x_coordinates = range(300)[0::50]
    # y_coordinates = range(350)[0::50]
    def draw_grid():
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

    def draw_letters():
        points = [(50,50), (100,50), (150, 50), (200,50), \
                    (50,100), (100,100), (150,100), (200,100), \
                    (50,150), (100,150), (150,150), (200,150), \
                    (50, 200), (100,200), (150, 200), (200,200)]
        letter_and_pos = zip(sample, points)

        for letter, pos in letter_and_pos:
            label = myfont.render(letter, 1, (255,255,0))
            # print pos
            screen.blit(label, pos)

    def draw_textbox():
        # screen.blit(answer, (50, 350))
        txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
        return txtbx

    def is_valid(word): # make it more descriptive and show why it's not valid
        # print 'target', word
        # print 'answers', answers
        if word in answers and word not in entries:
            print 'yes'
            return True
        else:
            print 'no'
            return False
    def update_score():
        score 

    # these were at the wrong level, changes didn't stick through
    sample = pick_letters()
    solver = bs.BoggleSolver(sample)
    answers = [word[0] for word in solver.solve()]
    print answers
    print type(answers[0])

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
        draw_grid()
        draw_letters()
        # update txtbx
        val = txtbx.update(events)
        if val is not None:
            # print val
            if is_valid(val):
                entries.append(val)
                # print val
            # print val
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()

if __name__ == '__main__': main()