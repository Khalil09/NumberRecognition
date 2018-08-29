import random
import collections
import numpy as np
from mnist import MNIST

def openTreatedTrain():
    mndata = MNIST('../img/testing')
    images, labels = mndata.load_testing()

    images = count_line_loop(images)

    del labels[-1]
    Testing = collections.namedtuple('Testing', ['images', 'labels'])

    return Testing(np.array(images), np.array(labels))



def openTreadtedTest():
    mndata = MNIST('../img/training')
    images, labels = mndata.load_training()

    images = count_line_loop(images)

    Training = collections.namedtuple('Training', ['images', 'labels'])

    return Training(np.array(images), np.array(labels))

def count_line_loop(images):
    count = 0
    aux = list()
    final = list() 
    for li in images:
        if aux != []:
            final.append(aux)
        aux = list()
        count = 0
        for i in range(len(li)-1):
            if li[i] != 0:
                count += 1
            if (i+1) % 28 == 0:
                aux.append(count)
                count = 0

        if li == images[-1]:
            final.append(aux)

    return final
