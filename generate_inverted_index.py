from tokenizer import tokenize
from fetch import fetch_column
import argparse
import csv

def build_inverted_index(docs, tokens):
    inv_index = {}
    for token in tokens:
        inv_index[token] = [0]
    for i in range(100):
        for j in range(500):
            if tokens[j] in docs[i]:
                inv_index[tokens[j]][0] += 1
                inv_index[tokens[j]].append(i)
    return inv_index

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Inverted Index')
    parser.add_argument('address', help='csv address', action='store')
    parser.add_argument('tokenize', help='type of tokenization: simple or pro', default='simple')
    args = parser.parse_args()
    csv_address = args.address
    tokenize_type = args.tokenize
    contents = fetch_column(csv_address, 'content')
    tokens = tokenize(tokenize_type, contents)
    inverted_index = build_inverted_index(contents, tokens)
    w = csv.writer(open("inverted_index.csv", "w"))
    for key, val in inverted_index.items():
        w.writerow([key, val])
