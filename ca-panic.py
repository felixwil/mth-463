import pycxsimulator
import numpy as np
from pylab import *
from sys import argv
from time import time

n = int(argv[1]) # size of space: n x n
p = float(argv[2]) # probability of initially panicky individuals
gens = 0
filled = False

def nparametersetting(val=n):
    global n
    n = int(val)
    return val

def pparametersetting(val=p):
    global p
    p = val
    return val

def initialize():
    global config, nextconfig, gens
    gens = 0
    # https://stackoverflow.com/questions/64862810/generating-random-binary-array-in-numpy-with-varying-probabilities-given-by-indi
    config = np.random.choice([0, 1], p=[1-p, p], size=(n, n))
    nextconfig = zeros([n, n])
    
def observe():
    global config, nextconfig
    # cla()
    # imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)

def update():
    global config, nextconfig, gens
    gens += 1
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            nextconfig[x, y] = 1 if count >= 4 else 0
    if np.sum(config) == n*n:
        exit(0)
    # if gens == 100:
    #     exit(1)
    if np.sum(np.abs(config - nextconfig)) == 0:
        exit(1)
    config, nextconfig = nextconfig, config

initialize()
for _ in range(100):
    update()
# gui = pycxsimulator.GUI(parameterSetters=[nparametersetting, pparametersetting])
# # gui.start(func=[initialize, observe, update])
# gui.modelInitFunc = initialize
# gui.modelDrawFunc = observe
# gui.modelStepFunc = update
# gui.runEvent()
