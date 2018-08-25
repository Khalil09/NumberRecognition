import random
from mnist import MNIST

def openTesting() :
    mndata = MNIST('../img/testing')

    images, labels = mndata.load_testing()

    index = random.randrange(0, len(images))  # choose an index ;-)
    print(mndata.display(images[index]))

def openTraining() :
    mndata = MNIST('../img/training')

    images, labels = mndata.load_training()

    index = random.randrange(0, len(images))  # choose an index ;-)
    print(mndata.display(images[index]))
