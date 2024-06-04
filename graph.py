import numpy as np
from matplotlib import pyplot

class Graph:
    def __init__(self, title, domain, winsize, xlabel, ylabel):
        self.startpos, self.endpos = domain

        pyplot.rcParams['toolbar'] = 'None'
        pyplot.figure(figsize=(winsize[0], winsize[1]))
        pyplot.axis([self.startpos, self.endpos, 0, 1])
        pyplot.xlabel(xlabel)
        pyplot.ylabel(ylabel)
        pyplot.title(title)
        pyplot.grid(True)

    def plot_mf(self, function, color, legend=None, shaded=False):
        xvals = np.arange(self.startpos, self.endpos, 0.1)
        yvals = np.vectorize(function, otypes=[float])(xvals)
        pyplot.plot(xvals, yvals, color=color, linestyle='-', label=legend)
        if shaded:
            pyplot.fill_between(xvals, yvals)
        pyplot.legend()
        pyplot.draw()

    def plot_line(self, x, legend):
        pyplot.axvline(x, color='black', linestyle='--', label=f'{legend} (x = {x:.2f})')
        pyplot.legend()
        pyplot.show()

    def plot_point(self, x, y):
        pyplot.scatter(x, y, color='black', label=f'({x}, {y})')
        pyplot.show()
