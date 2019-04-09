import acquire_zillow
import pandas as pd 
import numpy as np

def single_unit(df):
    single = ['Single Family Residential', 'Condominium', 'Mobile Home','Residential General', 'Townhouse']
    df = df[df.unitcnt == 1]
    df = df[df.propertylandusedesc.isin(single)]
    df = df[df.bathroomcnt >= 1]
    df = df[df.bedroomcnt >= 1]
    return df

def make_non_numeric(df):
    for col in ('id', 'parcelid', 'fips', 'rawcensustractandblock', 'regionidcity', 'regionidcounty', 'regionidneighborhood', 'regionidzip', 'yearbuilt', 'assessmentyear', 'taxdelinquencyyear', 'censustractandblock'):
        df[col] = df[col].astype(str)
    return df

