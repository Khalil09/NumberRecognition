# loading libraries
import readfiles as rf
from pathlib import Path
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


class LearnAlgorithms(object):

    def __init__(self):
        train = rf.openTraining()
        self.X_train = train.images
        self.Y_train = train.labels

        test = rf.openTesting()
        self.X_test = test.images
        self.Y_test = test.labels

    def knnLearn(self, k, train):
        # instantiate learning model (k = 3)
        knn = KNeighborsClassifier(n_neighbors=k)

        if  Path('../models/KnnModel.pkl').is_file() and not train:
            self.log("Loading KNN Model")
            knn = joblib.load('../models/KnnModel.pkl')
        else:
            # fitting the model
            self.log("Fitting KNN Model")
            knn.fit(self.X_train, self.Y_train)
            joblib.dump(knn, '../models/KnnModel.pkl')
        # predict the response
        self.log("Predicting KNN Tests")
        pred = knn.predict(self.X_test)
        # evaluate accuracy
        self.log("KNN Accuracy Score: {}".format(accuracy_score(self.Y_test, pred)))

    def ldaLearn(self, train):
        clf = LinearDiscriminantAnalysis()

        if  Path('../models/LdaModel.pkl').is_file() and not train:
            self.log("Loading LDA Model")
            clf = joblib.load('../models/LdaModel.pkl')
        else:
            # fitting the model
            self.log("Fitting LDA Model")
            clf.fit(self.X_train, self.Y_train)
            joblib.dump(knn, '../models/LdaModel.pkl')
        # predict the response
        self.log("Predicting LDA Tests")
        pred = clf.predict(self.X_test)
        # evaluate accuracy
        self.log("KNN Accuracy Score: {}".format(accuracy_score(Y_test, pred)))

    def log(self, msg):
        print('[Learn] {}'.format(msg))
