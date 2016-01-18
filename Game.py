import sys, pygame
import random
import eztext
import BoggleSolver as bs

# IMPORTANT TODO: Decide where the letter generating methods are going to be called,
# at the moment this won't run in Main.py, but 

class Game():

    def __init__(self):
        self.sample = []
        self.answers = []
        self.entries = []
        self.score = []

    def pick_letters():
        alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        self.sample = random.sample(alphabet, 16)
        return sample

    def generate_answers():
        solver = bs.BoggleSolver(sample)
        self.answers = [word[0] for word in solver.solve()]

    #should the drawing graphics methods really be here?
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
            label = myfont.render(letter, 1, (225,225,0))
            screen.blit(label, pos)

    def draw_textbox():
        # screen.blit(answer, (50, 350))
        txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
        return txtbx

    def is_valid(word): # make it more descriptive and show why it's not valid
        # print 'target', word
        # print 'answers', answers
        if word in self.answers and word not in self.entries:
            print 'yes'
            update_score(word)
            return True
        else:
            print 'no'
            return False

    def update_score(word):
        self.score += len(word)

