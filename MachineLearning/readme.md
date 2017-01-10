# Supervised Classification Algorithms

## Naive Bayes
#### from sklearn.naive_bayes import GaussianNB
#### clf = GaussianNB()
#### clf.fit(features_train, labels_train)

## Support Vector Machines
#### from sklearn import svm
#### clf = svm.SVC(kernel='linear')
#### clf.fit(features_train, labels_train)

## Decision Trees
#### from sklearn import tree
#### clf = tree.DecisionTreeClassifier(min_samples_split=2)
#### clf.fit(features_train, labels_train)
