import random
import collections
import numpy as np
from mnist import MNIST

def openTesting() :
    mndata = MNIST('../img/testing')
    images, labels = mndata.load_testing()

    del labels[-1]
    Testing = collections.namedtuple('Testing', ['images', 'labels'])

    return Testing(np.array(images), np.array(labels))

def openTraining() :
    mndata = MNIST('../img/training')
    images, labels = mndata.load_training()

    Training = collections.namedtuple('Training', ['images', 'labels'])

    return Training(np.array(images), np.array(labels))
