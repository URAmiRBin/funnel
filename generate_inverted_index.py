from tokenizer import tokenize
from fetch import fetch_column
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Inverted Index')
    parser.add_argument('address', help='csv address', action='store')
    parser.add_argument('tokenize', help='type of tokenization: simple or pro', default='simple')
    args = parser.parse_args()
    csv_address = args.address
    tokenize_type = args.tokenize
    contents = fetch_column(csv_address, 'content')
    tokens = tokenize(tokenize_type, contents)
