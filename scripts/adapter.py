import learnAlgorithms as learn

class Adapter(object):

    def __init__(self, algorithm, k, td, train):
        self.algorithm = algorithm
        self.k = k
        self.td = td
        self.train = train
        self.la = learn.LearnAlgorithms(treated_data=td)

    def run(self):
        if self.train:
            self.log("Training Model is Enabled")
        else:
            self.log("Training Model is Disabled")

        if self.algorithm == 'knn':
            self.log("Learning Algorithm set to KNN")
            self.log("K Value is set to {}".format(self.k))
            self.la.knnLearn(self.k, self.train)
        elif self.algorithm == 'lda':
            self.log("Learning Algorithm set to LDA")
            self.la.ldaLearn(self.train)
        else:
            self.log("Learning Algorithm set to Both")
            self.log("K Value is set to {}".format(self.k))
            self.la.knnLearn(self.k, self.train)
            self.la.ldaLearn(self.train)

    def log(self, msg):
        print('[Adapter] {}'.format(msg))
