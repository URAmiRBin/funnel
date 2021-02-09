import pickle
from tfidf import tf_idf, querySimilarity
from Heap import Heap
from fetch import fetch_column
import heapq
import operator
import sys

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

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

def runEngine(tokenizer_type, address):
    print("RUNNING ENGINE ...")
    inverted_index = load_obj("INVERTED INDEX " + tokenizer_type + "_" + address)
    tfidfs = load_obj("CHAMPIONS " + tokenize_type + "_" + address)
    
    query = ""

    while True:
        query = input("QUERY :>")
        if query == "!q": break

        queryToken = query.split(" ")
        queryw = tf_idf(queryToken, inverted_index, False)


        h = Heap()    

        for i in range(len(tfidfs)):
            if bool(set(queryToken) & set(tfidfs[i].keys())):
                sim = querySimilarity(queryw, tfidfs[i])
                if sim != 0:
                    h.addnSort([i, sim])

        k = 10
        result = h.getFirstK(k)
        titles = fetch_column(address, 'title')
        for i in range(k):
            print(titles[result[i][0]][::-1])

        
if __name__ == "__main__":
    tokenize_type = sys.argv[2]
    address = sys.argv[1]
    runEngine(tokenize_type, address)
