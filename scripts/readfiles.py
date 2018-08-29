import random
import collections
import numpy as np
from mnist import MNIST
from imageProcessing import imageProcessing as iP

def processImage(images, ip):
    if ip == 'normalLines':
        return iP().normalLines(images)
    else:
        return images

def openTesting(ip) :
    mndata = MNIST('../img/testing')
    images, labels = mndata.load_testing()

    images = processImage(images, ip)

    del labels[-1]
    Testing = collections.namedtuple('Testing', ['images', 'labels'])

    return Testing(np.array(images), np.array(labels))

def openTraining(ip) :
    mndata = MNIST('../img/training')
    images, labels = mndata.load_training()

    images = processImage(images, ip)

    Training = collections.namedtuple('Training', ['images', 'labels'])

    return Training(np.array(images), np.array(labels))
