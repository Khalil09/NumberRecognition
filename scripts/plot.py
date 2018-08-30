import matplotlib.pyplot as plt
import numpy as np
import itertools

class Plot(object):

    @staticmethod
    def plot_confusion_matrix(cm, classes,
                              normalize=False,
                              title='Matriz de confusão',
                              cmap=plt.cm.Blues):

        plt.figure()
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes)
        plt.yticks(tick_marks, classes)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            if normalize:
                string = "{0:.0f}%".format(cm[i, j]*100)
            else:
                string = "{}".format(cm[i, j])


            plt.text(j, i, string,
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('classes reais')
        plt.xlabel('classes preditas')
        plt.show()