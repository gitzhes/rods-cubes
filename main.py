import numpy as np
import pandas as pd
import argparse


def process_csv(csv):
    df = pd.read_csv(csv, sep=",", header=None,
                     usecols=[0, 1], names=["v1", "v2"], dtype={"v1": "int64", "v2": "int64"})
    rows = len(df.index)
    if rows == 0:
        print("Number of rods could be removed: ", 0)
    else:
        df['sv'] = np.where(df['v1'] >= df['v2'], df['v2'], df['v1'])
        df['bv'] = np.where(df['v1'] >= df['v2'], df['v1'], df['v2'])
        df['val'] = df[['sv', 'bv']].astype(str).agg('-'.join, axis=1)
        df = df.drop(['v1', 'v2', 'sv', 'bv'], axis=1)
        #print(df.head())
        df['counts'] = 0
        df = df.groupby('val').agg({'counts': 'count'})
        # print(df.head())
        rods = df['counts'].sum() - len(df.index)
        print(df.head())
        #print(df.head())
        print("Number of rods could be removed: ", rods)


def main(csv):
    if not csv.lower().endswith('json'):
        process_csv(csv)
    else:
        print("Number of rods could be removed: ", 0)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--inputCSV", required=True, help="path to CSV file where ")
    args = vars(ap.parse_args())

    main(args['inputCSV'])

