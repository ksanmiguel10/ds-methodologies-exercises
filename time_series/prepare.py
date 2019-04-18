import requests
import json
import pandas as pd
import numpy as np
import acquire

def make_datetime(df[col]):
    pd.to_datetime(df[col], utc=True)

def split_date_series(series: pd.Series) -> tuple:
    """
    Return six columns: year, quarter, month, day, weekday #, and whether it's a weekday (1) or weekend (0)
    """
    year = series.dt.year.rename("year")
    quarter = series.dt.quarter.rename("quarter")
    month = series.dt.month.rename("month")
    day = series.dt.day.rename("day")
    weekday = series.dt.weekday.rename("weekday")
    is_weekday = (series.dt.weekday < 5).rename("is_weekday")
    return year, quarter, month, day, weekday, is_weekday

# df = pd.concat([df, *split_date_series(df.sale_date)], axis=1)

def make_dt_index(df[col]):
    df.set_index(df[col], inplace=True)