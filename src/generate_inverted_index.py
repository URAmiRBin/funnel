from tokenizer import tokenize
from normalizer import normilize
from stemmer import stem_list
from fetch import fetch_column
from tfidf import tf_idf
import argparse
import heapq
import operator
import pickle
import csv

def build_inverted_index(docs, dic):
    inv_index = {}
    for token in dic:
        inv_index[token] = [0]
    for i in range(len(docs)):
        for j in range(len(docs[i])):
            inv_index[docs[i][j]][0] += 1
            inv_index[docs[i][j]].append(i)
    return inv_index

def build_dictionary(tokens):
    dic = []
    for i in range(len(tokens)):
        for j in range(len(tokens[i])):
            dic.append(tokens[i][j])
    dic = list(dict.fromkeys(dic))
    return dic


def writeObj(name, dic, tType, address):
    with open('obj/'+ name + " " + tType + "_" + address + '.pkl', 'wb') as f:
        pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)

def getChampions(tokens, inverted_index):
    tfidfs = []
    for i in range(len(tokens)):
        tfidfs.append(tf_idf(tokens[i], inverted_index, False))

    champions_term = {}
    champions_list = {}

    # TODO: Optimize this mess
    for term in inverted_index:
        champions_term[term] = [None] * inverted_index[term][0]
        for i in range(0, inverted_index[term][0]):
            champions_term[term][i] = tfidfs[inverted_index[term][i + 1]][term]

    for term in champions_term:
        y = list(zip(*heapq.nlargest(10, enumerate(champions_term[term]), key=operator.itemgetter(1))))[0]
        champions_list[term] = list(y)


    for term in champions_list:
        l = min(10, len(champions_list[term]))
        for i in range(l):
            champions_list[term][i] = inverted_index[term][champions_list[term][i] + 1]

    return champions_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Inverted Index')
    parser.add_argument('address', help='csv address', action='store')
    parser.add_argument('tokenize', help='type of tokenization: simple or pro', default='simple')
    args = parser.parse_args()
    csv_address = args.address
    tokenize_type = args.tokenize
    
    print("READING ", csv_address)
    contents = fetch_column(csv_address, 'content')
    tokens = tokenize(tokenize_type, contents)
    
    print("TOKENIZING ", tokenize_type)
    if tokenize_type == 'pro':
        tokens = normilize(tokens)
        tokens = stem_list(tokens)
    
    print("BUILDING DICTIONARY AND INVERTED INDEX")
    dictionary = build_dictionary(tokens)
    inverted_index = build_inverted_index(tokens, dictionary)
    
    print("WRITING INDEX AND SCORES")
    writeObj("INVERTED INDEX", inverted_index, tokenize_type, csv_address)

    tfidfs = []
    for i in range(len(tokens)):
        tfidfs.append(tf_idf(tokens[i], inverted_index, True))

    writeObj("TFIDF", tfidfs, tokenize_type, csv_address)
