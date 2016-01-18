import re
import random

#TO-DO:: regex matching not working so well so commented it out, fix it

class BoggleSolver():
    def __init__(self, sample):
        self.sample = [letter.lower() for letter in sample]
        # self.alphabet = ''.join(self.sample)
        self.matrix = [self.sample[i:i+4] for i in xrange(0, len(self.sample), 4)]
        self.nrows = len(self.matrix)
        self.ncols = len(self.matrix[0])
        # print self.matrix

    def solve(self):
        # alphabet from words in the board
        alphabet = ''.join(self.sample)
        print alphabet
        bogglable = re.compile('[' + alphabet + ']{3,}$', re.I).match
        # bogglable = re.compile('[' + alphabet + ']{3,}$', re.I).match #does this return a fn whutt
        # add word from dictionary file if it is a possible play given the board
        # words = set(word.rstrip('\r\n') for word in open('words.txt') if bogglable(word))
        words = set(word.rstrip('\r\n') for word in open('words.txt') if len(word.rstrip('\r\n'))>2)
        # make prefix set from the possible words 
        prefixes = set(word[:i] for word in words for i in range(2, len(word)+1))

        for y,row in enumerate(self.matrix):
            for x, letter in enumerate(row):
                for result in self._extending(words, prefixes, letter,((x, y),)):
                    yield result

    def _extending(self, words, prefixes, prefix, path):
        if prefix in words:
            yield (prefix, path)
        for (nx, ny) in self._neighbors(path[-1]):
            if (nx, ny) not in path:
                prefix1 = prefix + self.matrix[ny][nx]
                if prefix1 in prefixes:
                    for result in self._extending(words, prefixes, prefix1, path + ((nx, ny),)):
                        yield result

    def _neighbors(self, (x, y)):
        for nx in range(max(0, x-1), min(x+2, self.ncols)):
            for ny in range(max(0, y-1), min(y+2, self.nrows)):
                yield (nx, ny)

# alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
# sample = random.sample(alphabet, 16)
# solver = BoggleSolver(sample)
# print [word[0] for word in solver.solve()]