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
    for col in ('gender', 'annual_income', 'spending_score'):
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
