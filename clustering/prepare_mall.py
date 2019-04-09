import acquire_mall
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def is_outlier(df):
    q1 = df.annual_income.quantile(.25)
    q3 = df.annual_income.quantile(.75)
    iqr = q3 - q1
    df[df.annual_income > (q3 + 1.5 * iqr)]
    df['annual_income_outliers'] = df.annual_income.apply(lambda x: max([x - (q3 + 1.5 * iqr), 0]))
    return df

def encode_mall(df):
    for col in ('gender'):
        encoder=LabelEncoder()
        encoder.fit(df[col])
        new_col = col + '_encoded'
        print(new_col)
        df[new_col] = encoder.transform(df[col])
    return df

def prepare_mall(df):
    df = is_outlier(df)
    df = encode_mall(df)
    return df

def summarize_df(df):
    print("\nRows & Columns:\n")
    print(df.shape)
    print("\nColumn Info:\n")
    print(df.info())
    print("\nFirst 5 rows:\n")
    print(df.head())
    print("\nLast 5 rows:\n")
    print(df.tail())
    print("\nMissing Values:\n")
    missing_vals = df.columns[df.isnull().any()]
    print(df.isnull().sum())
    print("\nSummary Stats:\n")
    print(df.describe())
    