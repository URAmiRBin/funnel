import pickle
from tfidf import tf_idf, querySimilarity
from Heap import Heap
from fetch import fetch_column
import sys

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def runEngine(tokenizer_type, address):
    print("RUNNING ENGINE ...")
    inverted_index = load_obj("INVERTED INDEX " + tokenizer_type + "_" + address)
    tfidfs = load_obj("TFIDF " + tokenize_type + "_" + address)
    
    query = ""

    while True:
        query = input("QUERY :>")
        if query == "!q": break

        queryToken = query.split(" ")
        queryw = tf_idf(queryToken, inverted_index)


        h = Heap()    

        for i in range(len(tfidfs)):
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
