from plot import Plot as Plot 
import readfiles as rf
import learnAlgorithms as learn

class Adapter(object):

    def __init__(self, algorithm, k, train, ip, confPlot):
        self.algorithm = algorithm
        self.k = k
        self.train = train
        self.confPlot = confPlot
        self.train = rf.openTraining(ip)
        self.test = rf.openTesting(ip)

        self.la = learn.LearnAlgorithms(self.train, self.test)

    def run(self):
        normalized = True if self.confPlot == "normalized" else False

        if self.train:
            self.log("Training Model is Enabled")
        else:
            self.log("Training Model is Disabled")

        if self.algorithm == 'knn':
            self.log("Learning Algorithm set to KNN")
            self.log("K Value is set to {}".format(self.k))
            cof_mat = self.la.knnLearn(self.k, self.train)

            if self.confPlot != "False":
                Plot.plot_confusion_matrix(cof_mat,
                                           [0,1,2,3,4,5,6,7,8,9],
                                           title="Matriz de confusão KNN com K = " + str(self.k),
                                           normalize=normalized)

        elif self.algorithm == 'lda':
            self.log("Learning Algorithm set to LDA")
            cof_mat = self.la.ldaLearn(self.train)

            if self.confPlot != 'False':
                Plot.plot_confusion_matrix(cof_mat, 
                                           [0,1,2,3,4,5,6,7,8,9],
                                           title="Matriz de confusão LDA",
                                           normalize=normalized)
        else:
            self.log("Learning Algorithm set to Both")
            self.log("K Value is set to {}".format(self.k))
            self.la.knnLearn(self.k, self.train)
            self.la.ldaLearn(self.train)

    def log(self, msg):
        print('[Adapter] {}'.format(msg))
