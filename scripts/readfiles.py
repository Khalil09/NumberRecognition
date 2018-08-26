import random
from mnist import MNIST
import collections

def openTesting() :
    mndata = MNIST('../img/testing')
    images, labels = mndata.load_testing()

    del labels[-1]
    Testing = collections.namedtuple('Testing', ['images', 'labels'])

    return Testing(images, labels)

def openTraining() :
    mndata = MNIST('../img/training')
    images, labels = mndata.load_training()

    Training = collections.namedtuple('Training', ['images', 'labels'])

    return Training(images, labels)
