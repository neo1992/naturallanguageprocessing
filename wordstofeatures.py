import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.corpus import movie_reviews
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
feauturesets = [(find_features(rev), category) for (rev, category) in documents]

training_set = feauturesets[:1900]
testing_set = feauturesets[1900:]

#classifier = nltk.NaiveBayesClassifier.train(training_set)

#Using the saved classifier object using pickle
classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Original Naive Bayes Algo Accuracy percent: ", (nltk.classify.accuracy(classifier, testing_set)) *100)
classifier.show_most_informative_features(15)

# #Saving the classifier object using pickle
# save_classifier = open("naivebayes.pickle", "wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

#Multiomial Classifier
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier Accuracy percent: ", (nltk.classify.accuracy(MNB_classifier, testing_set)) *100)

#GaussianNB, BernoulliNB
# Gaussian_classifier = SklearnClassifier(GaussianNB())
# Gaussian_classifier.train(training_set)
# print("Gaussian_classifier Accuracy percent: ", (nltk.classify.accuracy(Gaussian_classifier, testing_set)) *100)

Bernoulli_classifier = SklearnClassifier(BernoulliNB())
Bernoulli_classifier.train(training_set)
print("Bernoulli_classifier Accuracy percent: ", (nltk.classify.accuracy(Bernoulli_classifier, testing_set)) *100)

# LogisticRegression, SGDClassifier
# SVC, LinearSVC, NuSVC

# LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
# LogisticRegression_classifier.train(training_set)
# print("LogisticRegression_classifier Accuracy percent: ", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)) *100)

Sgd_classifier = SklearnClassifier(SGDClassifier())
Sgd_classifier.train(training_set)
print("Sgd_classifier Accuracy percent: ", (nltk.classify.accuracy(Sgd_classifier, testing_set)) *100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier Accuracy percent: ", (nltk.classify.accuracy(SVC_classifier, testing_set)) *100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier Accuracy percent: ", (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) *100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier Accuracy percent: ", (nltk.classify.accuracy(NuSVC_classifier, testing_set)) *100)


voted_classifier = VoteClassifier(classifier,MNB_classifier,LinearSVC_classifier,NuSVC_classifier,Bernoulli_classifier,SVC_classifier,Sgd_classifier)
print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

print("CLassification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0]))
print("CLassification:", voted_classifier.classify(testing_set[1][0]), "Confidence %:",voted_classifier.confidence(testing_set[1][0]))
print("CLassification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0]))
print("CLassification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0]))
print("CLassification:", voted_classifier.classify(testing_set[4][0]), "Confidence %:",voted_classifier.confidence(testing_set[4][0]))
