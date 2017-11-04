# __author__ Udacity

import random

def makeTerrainData(n_points = 1000):
    n_points = 1000
    random.seed(42) # same random number everytime
    grade = [random.random() for ii in range(0,n_points)]
    print (grade)
    bumpy = [random.random() for ii in range (0,n_points)]
    print (bumpy)
    error = [random.random() for ii in range(0,n_points)]
    print(error)

    y = [round(grade[ii]*bumpy[ii]+0.3+0.1*error[ii]) for ii in range(0,n_points)]
    print(y)
    if grade[ii]>0.8 or bumpy[ii]>0.8:
        y[ii] = 1.0
    print(y)

    ### split into train/test sets
    X = [[gg,ss] for gg, ss in zip(grade, bumpy)]
    print(X)
    split = int(0.75*n_points)
    #print(split)
    X_train = X[0:split]
    X_test = X[split:]
    y_train = y[0:split]
    y_test  = y[split:]

    grade_sig = [X_train[ii][0] for ii in range(0,len(X_train)) if y_train[ii] == 0]
    bumpy_sig = [X_train[ii][1] for ii in range(0,len(X_train)) if y_train[ii] == 0]
    grade_bkg = [X_train[ii][0] for ii in range(0,len(X_train)) if y_train[ii] == 1]
    bumpy_bkg = [X_train[ii][1] for ii in range(0,len(X_train)) if y_train[ii] == 1]
    print(grade_sig)

    print ('\n')
    training_data = {"fast":{"grade":grade_sig, "bumpiness": bumpy_sig}, "slow":{"grade":grade_bkg, "bumpiness":bumpy_bkg}}
    print(training_data)

    grade_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 1]
    bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 1]

    test_data = {"fast": {"grade": grade_sig, "bumpiness": bumpy_sig}
        , "slow": {"grade": grade_bkg, "bumpiness": bumpy_bkg}}

    print(test_data)

    return X_train, y_train, X_test, y_test