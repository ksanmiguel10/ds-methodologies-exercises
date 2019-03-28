import acquire
import pandas as pd

#iris
def drop_columns(df):
    df.drop(columns='species_id', inplace=True)
    df.drop(columns='measurement_id', inplace=True)
    return df

def rename_columns(df):
    df.rename(columns={"species_name":"species"}, inplace=True)    
    return df

def encode_iris(df):
    encoder = LabelEncoder()
    encoder.fit(df.species)
    return df.assign(species = encoder.transform(df.species))
    
def prep_iris(df):
    df = drop_columns(df)
    df = rename_columns(df)
    df = encode_iris(df)
    return df

#titanic
def missing_values(df2):
    df2.embark_town.fillna('Other', inplace=True)
    df2.embarked.fillna('O', inplace=True)
    return df2

def drop_columns(df2):
    df2.drop(columns='deck', inplace=True)
    return df2

def encode_embarked(df2):
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    encoder.fit(df2.embarked)
    df2.embarked = encoder.transform(df2.embarked)
    return df2
    
def scale_data(df2):    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    train, test = train_test_split(df2)
    scaler = MinMaxScaler()
    scaler.fit(train[['fare', 'age']])
    train[['fare', 'age']] = scaler.transform(train[['fare', 'age']])
    test[['fare', 'age']] = scaler.transform(test[['fare', 'age']])
    return df2
    
def prep_titanic(df2):
    df = missing_values(df2)
    df = drop_columns(df2)
    df = encode_embarked(df2)
    df = scale_data(df2)
    return df2