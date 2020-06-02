import argparse
import pandas as pd


def fetch_column(raw_csv, column_name):
    df = pd.read_csv(raw_csv)
    return df[column_name]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='csv fetch data')
    parser.add_argument('address', help='csv address', action='store')
    args = parser.parse_args()
    raw_csv = args.address
    urls = fetch_column(raw_csv, 'url')
    print(urls[0])

