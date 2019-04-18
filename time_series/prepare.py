import requests
import json
import pandas as pd
import numpy as np
import acquire

def make_datetime(df):
    datetime_format = '%a, %d %b %Y %H:%M:%S %Z'
    df['sale_date'] = pd.to_datetime(df['sale_date'], format=datetime_format, utc=True)
    return df

def add_date_parts(df):
    df['year'] = df.sale_date.dt.year
    df['quarter'] = df.sale_date.dt.quarter
    df['month'] = df.sale_date.dt.month
    df['day'] = df.sale_date.dt.day
    df['weekday'] = df.sale_date.dt.day_name().str[:3]
    df['is_weekend'] = df.weekday.str.startswith('S')
    return df

def make_sales_total(df):
    df['sale_total'] = df.sale_amount * df.item_price
    return df.rename(columns={'sale_amount':'quantity'})

def add_sales_difference(df):
    df['diff_from_last_day'] = df.sale_total.diff()
    return df

def make_dt_index(df):
    return df.set_index('sale_date', inplace=True)

def aggregate_by_weekday(df):
    return df.groupby('weekday')[['sale_total', 'quantity']].agg(['median', 'sum'])

def prep_store_data(df):
    df = make_datetime(df)
    df = add_date_parts(df)
    df = make_sales_total(df)
    df = add_sales_difference(df)
    return df
