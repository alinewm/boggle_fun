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

    def pick_letters(self):
        alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        self.sample = random.sample(alphabet, 16)
        # return self.sample

    def generate_answers(self):
        solver = bs.BoggleSolver(sample)
        self.answers = [word[0] for word in solver.solve()]

    def is_valid(self, word): # make it more descriptive and show why it's not valid
        # print 'target', word
        # print 'answers', answers
        if word in self.answers and word not in self.entries:
            print 'yes'
            return True
        else:
            print 'no'
            return False

    def update_score(self, word):
        self.score += len(word)

    def update_entries(self, word):
        self.entries.append(word)

