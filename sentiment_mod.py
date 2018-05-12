import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

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

short_pos = open("positive.txt","r").read()
short_neg = open("negative.txt","r").read()

documents = []
all_words = []

#j is adjective, r is adverb and v is verb
#allowed_word_types = ["J", "R", "V"]
allowed_word_types = ["J"]

for p in short_pos.split('\n'):
    documents.append((p, "pos"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for p in short_neg.split('\n'):
    documents.append((p, "neg"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

save_documents = open("pickled_algos/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

save_word_features = open("pickled_algos/word_features.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
feauturesets = [(find_features(rev), category) for (rev, category) in documents]

save_featuresets = open("pickled_algos/featuresets.pickle", "wb")
pickle.dump(feauturesets, save_featuresets)
save_featuresets.close()

random.shuffle(feauturesets)

training_set = feauturesets[:10000]
testing_set = feauturesets[10000:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo Accuracy percent: ", (nltk.classify.accuracy(classifier, testing_set)) *100)
classifier.show_most_informative_features(15)

######
save_classifier = open("pickled_algos/originalnaivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

#Multiomial Classifier
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier Accuracy percent: ", (nltk.classify.accuracy(MNB_classifier, testing_set)) *100)

save_classifier = open("pickled_algos/MNB_classifier.pickle", "wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

Bernoulli_classifier = SklearnClassifier(BernoulliNB())
Bernoulli_classifier.train(training_set)
print("Bernoulli_classifier Accuracy percent: ", (nltk.classify.accuracy(Bernoulli_classifier, testing_set)) *100)

save_classifier = open("pickled_algos/Bernoulli_classifier.pickle", "wb")
pickle.dump(Bernoulli_classifier, save_classifier)
save_classifier.close()


Sgd_classifier = SklearnClassifier(SGDClassifier())
Sgd_classifier.train(training_set)
print("Sgd_classifier Accuracy percent: ", (nltk.classify.accuracy(Sgd_classifier, testing_set)) *100)

save_classifier = open("pickled_algos/Sgd_classifier.pickle", "wb")
pickle.dump(Sgd_classifier, save_classifier)
save_classifier.close()

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier Accuracy percent: ", (nltk.classify.accuracy(SVC_classifier, testing_set)) *100)

save_classifier = open("pickled_algos/SVC_classifier.pickle", "wb")
pickle.dump(SVC_classifier, save_classifier)
save_classifier.close()

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier Accuracy percent: ", (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) *100)

save_classifier = open("pickled_algos/LinearSVC_classifier.pickle", "wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier Accuracy percent: ", (nltk.classify.accuracy(NuSVC_classifier, testing_set)) *100)

save_classifier = open("pickled_algos/NuSVC_classifier.pickle", "wb")
pickle.dump(NuSVC_classifier, save_classifier)
save_classifier.close()


# voted_classifier = VoteClassifier(classifier,MNB_classifier,LinearSVC_classifier,NuSVC_classifier,Bernoulli_classifier,SVC_classifier,Sgd_classifier)
# print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)
#
# print("CLassification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0]))
# print("CLassification:", voted_classifier.classify(testing_set[1][0]), "Confidence %:",voted_classifier.confidence(testing_set[1][0]))
# print("CLassification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0]))
# print("CLassification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0]))
# print("CLassification:", voted_classifier.classify(testing_set[4][0]), "Confidence %:",voted_classifier.confidence(testing_set[4][0]))
