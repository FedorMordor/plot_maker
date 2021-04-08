

from abc import ABC, abstractmethod
from collections import OrderedDict
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

class PlotMaker():

    def __init__(self):
      
        self.figsize = (7, 5)
        self.big_fontsize = 15
        self.medium_fontsize = 12
        self.save = True
        self.scilimits = (0, 0)

    def set_params(self, **kwargs):
        self.__dict__.update(**kwargs)

    def make_plot(self, conts, xlabel=None, ylabel=None, legend=None):

        # preparations
        assert not ((xlabel is None) and (ylabel is None)), "Set xlabel and ylabel"

        if legend is None:
            for i, element in enumerate(conts):
                plt.plot(*element.T, linewidth=1.5)
        else:
            for i, element in enumerate(conts):
                plt.plot(*element.T, label=legend[i], linewidth=1.5)
                plt.legend(fontsize=self.medium_fontsize)

        plt.grid(True)
        plt.ticklabel_format(style='sci', scilimits=self.scilimits)
        plt.tick_params(labelsize=self.medium_fontsize)
        plt.xlabel(xlabel, fontsize=self.big_fontsize)
        plt.ylabel(ylabel, fontsize=self.big_fontsize)
        plt.show()

big_plot_params = {'figsize':(15, 10),
        'big_fontsize': 20,
        'medium_fontsize': 15,
        'scilimits':(0, 0)}

small_plot_params = {'figsize':(7, 5),
        'big_fontsize': 15,
        'medium_fontsize': 12,
        'scilimits':(0, 0)}

