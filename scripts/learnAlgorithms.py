# loading libraries
from pathlib import Path
import numpy as np
import readfiles as rf
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def knnLearn():
    train = rf.openTraining()
    X_train = np.array(train.images)
    Y_train = np.array(train.labels)

    test = rf.openTesting()
    X_test = np.array(test.images)
    Y_test = np.array(test.labels)

    # instantiate learning model (k = 3)
    knn = KNeighborsClassifier(n_neighbors=3)

    if  Path('./model.pkl').is_file():
        knn = joblib.load('model.pkl')
    else:
        # fitting the model
        knn.fit(X_train, Y_train)
        joblib.dump(knn, 'model.pkl')



    print(len(Y_test))
    print(np.shape(Y_test))
    # predict the response
    pred = knn.predict(X_test)

    # evaluate accuracy
    print(accuracy_score(Y_test, pred))
