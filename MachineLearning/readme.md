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

# Regressions
## Linear Regression
## Removing Outliers

# Unsupervised Learning: 
## Clustering
### k-means
#### - (1) Assign
#### - (2) Optimize
####
## Feature Scaling
### - Scales feature between 0 and 1


# Text Learning
### Bag of Words
### Stemmer
#### - stemming should be done before 'bag of words' transformation
### TfIdf : term frequency, inverse document frequency
#### - Tf - Term frequency
#### - Idf - Weighting by how often word occurs in corpus
#### - TfIdf provides bigger weights to words which are rare

# Feature Selection
## Regularization
### Overfitting

# Principle Component Analysis
## Dimensionality reduction

# Cross Validation

