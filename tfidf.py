from collections import Counter, OrderedDict
import math

N = 10000
threshold = 0.05

def tf(termFreq):
    return 1 + math.log(termFreq, 10)

def idf(documentFrequency):
    return math.log(N / documentFrequency, 10)

def normalize(documentScores):
    denom = 0
    for term in documentScores:
        denom += documentScores[term]
    denom = math.sqrt(denom)
    for term in documentScores:
        documentScores[term] = documentScores[term] / denom

def indexElimination(documentScores):
    badKeys = []
    for term in documentScores:
        if documentScores[term] < threshold:
            badKeys.append(term)

    for i in range(len(badKeys)):
        del(documentScores[badKeys[i]])


def tf_idf(tokens, invIndex):
    docFrequency = Counter(tokens)
    
    for term in docFrequency:
        if term in invIndex:
            docFrequency[term] = tf(docFrequency[term]) * idf(invIndex[term][0])
    normalize(docFrequency)
    indexElimination(docFrequency)
    return docFrequency

def querySimilarity(queryVector, docVector):
    cosSim = 0
    for term in queryVector:
        if term in docVector:
            cosSim += queryVector[term] * docVector[term]
    return cosSim