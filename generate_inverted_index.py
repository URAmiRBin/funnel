from tokenizer import tokenize
from normalizer import normilize
from stemmer import stem_list
from fetch import fetch_column
from tfidf import tf_idf, querySimilarity
from Heap import Heap
import argparse
import csv
import codecs

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


def writeIndex(dic):
    keys = list(dic.keys())
    f = codecs.open("Inverted Index.txt", "w", "utf-8")
    for i in range(len(keys)):
        f.write(keys[i])
        f.write(",")
        temp = dic.get(keys[i])
        f.write(str(temp[0]))
        f.write("\n")
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Inverted Index')
    parser.add_argument('address', help='csv address', action='store')
    parser.add_argument('tokenize', help='type of tokenization: simple or pro', default='simple')
    args = parser.parse_args()
    csv_address = args.address
    tokenize_type = args.tokenize
    if csv_address == 'test':
        contents = [ 'بنا بر این من حوصله ام از مدرسه ها سر می رود',
                    'دانشگاه صنعتی امیر کبیر ریده',
                    'هیئت مدیره با نظام آموزشی نا آشنا هستند',
                    'برای ثبت نام درختها نمی توانسته ام',
                    'علی الخصوص تخت خواب ما هیچ کدام از مسخره ترین ها را نمی خواهد',
                    'من به درختان نگاه می کنم',
                    'شما به مدرسه ها می روید',
                    'آن ها دیروز تلویزیون تماشا کردند',
                    'من حوصله ام سر رفته است',
                    'بنابراین این آخر راه است',
                    'هیئت مدیره دانشگاه صنعتی امیر کبیر اعلام کرد ما ریدیم'
        ]
    else:
        contents = fetch_column(csv_address, 'content')
    tokens = tokenize(tokenize_type, contents)
    if tokenize_type == 'pro':
        tokens = normilize(tokens)
        tokens = stem_list(tokens)
    dictionary = build_dictionary(tokens)
    inverted_index = build_inverted_index(tokens, dictionary)

    queryw = tf_idf(['خون', 'انتقال'], inverted_index)

    h = Heap()    

    for i in range(len(tokens)):
        docw = tf_idf(tokens[i], inverted_index)
        sim = querySimilarity(queryw, docw)
        if sim != 0:
            h.addnSort([i, sim])

    k = 10
    result = h.getFirstK(k)
    titles = fetch_column(csv_address, 'title')
    for i in range(k):
        print(titles[result[i][0]])

