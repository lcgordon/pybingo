""" 
Main script for generating bingo boards
"""
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import random
import os

class pybingo(object):
    """Creates the pybingo object"""

    def __init__(self, save_dir, squares_csv, free_space, nboards=1, gridsize=5, title='Bingo!'):
        """ Creates bingo boards using matplotlib

        Parameters
        ----------
        save_dir : str
            Directory to save into
        squares_csv : str
            Location of csv file containing squares to draw from 
        free_space : str
            Individual string to use in center square
        nboards : int
            Number of boards to create; default 1 
        gridsize : int 
            Square sizing of grid; default 5 for a 5x5 grid 
        title : str
            Title for each board; default 'Bingo!'
        """
        print("Running pybingo!")
        # save directory setup: 
        self.SD = save_dir
        if not os.path.exists(self.SD):
            os.mkdir(self.SD)

        # load squares
        self.SQ = pd.read_csv(squares_csv, header=None, names=['squares', 'bad'])['squares'].to_numpy()
        self.FS = free_space
        self.GS = gridsize
        self.nboards = nboards
        self.title = title
        self.centerSquare = int(np.floor(self.GS**2 / 2))

        # set up line breaks:
        self.squares = []
        for i in range(len(self.SQ)):
            word = self.SQ[i]
            splitword = word.split(" ")
            newword = ""
            for j in range(len(splitword)):
                if j % 2 == 0 and j > 0: 
                    newword = newword + " \n" + splitword[j]
                else:
                    newword = newword + " " + splitword[j]
            self.squares.append(newword)

        # make boards:
        for b in range(self.nboards):

            random.shuffle(self.squares)

            fig, ax = plt.subplots(self.GS, self.GS, figsize=(12, 12))
            ax = ax.flatten()
            output = f"{self.SD}/board-{b}.png"

            for i, word in enumerate(self.squares[:self.GS**2]):
                axy = ax[i]
                axy.set_xticks([])
                axy.set_yticks([])
                if i == self.centerSquare:
                    axy.annotate(self.FS, xy=(0.5, 0.5), xycoords='axes fraction', horizontalalignment='center',
                        verticalalignment='center', fontsize=13)
                else:
                    axy.annotate(word, xy=(0.5, 0.5), xycoords='axes fraction', horizontalalignment='center',
                        verticalalignment='center', fontsize=13)

                    
            plt.suptitle(self.title, fontsize=45)
            plt.tight_layout()
            plt.savefig(output)
    print("Boards complete!")
    return

