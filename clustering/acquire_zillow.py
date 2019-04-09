import env
import pandas as pd

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_zillow_prop16():
    df = pd.read_sql('\
    SELECT * FROM properties_2016 prop16\
    JOIN predictions_2016 pred16 ON prop16.parcelid = pred16.parcelid\
    LEFT JOIN airconditioningtype act ON prop16.airconditioningtypeid = act.airconditioningtypeid\
    LEFT JOIN architecturalstyletype ast ON prop16.architecturalstyletypeid = ast.architecturalstyletypeid\
    LEFT JOIN buildingclasstype bct ON prop16.buildingclasstypeid = bct.buildingclasstypeid\
    LEFT JOIN heatingorsystemtype hst ON prop16.heatingorsystemtypeid = hst.heatingorsystemtypeid\
    LEFT JOIN propertylandusetype plt ON prop16.propertylandusetypeid = plt.propertylandusetypeid\
    LEFT JOIN storytype st ON prop16.storytypeid = st.storytypeid\
    LEFT JOIN typeconstructiontype tct ON prop16.typeconstructiontypeid = tct.typeconstructiontypeid;',\
    get_connection('zillow'))
    return df

def get_zillow_prop17():
    df2 = pd.read_sql('\
    SELECT * FROM properties_2017 prop17\
    JOIN predictions_2017 pred17 ON prop17.parcelid = pred17.parcelid\
    LEFT JOIN airconditioningtype act ON prop17.airconditioningtypeid = act.airconditioningtypeid\
    LEFT JOIN architecturalstyletype ast ON prop17.architecturalstyletypeid = ast.architecturalstyletypeid\
    LEFT JOIN buildingclasstype bct ON prop17.buildingclasstypeid = bct.buildingclasstypeid\
    LEFT JOIN heatingorsystemtype hst ON prop17.heatingorsystemtypeid = hst.heatingorsystemtypeid\
    LEFT JOIN propertylandusetype plt ON prop17.propertylandusetypeid = plt.propertylandusetypeid\
    LEFT JOIN storytype st ON prop17.storytypeid = st.storytypeid\
    LEFT JOIN typeconstructiontype tct ON prop17.typeconstructiontypeid = tct.typeconstructiontypeid;',\
    get_connection('zillow'))
    return df2

def merge_zillow():
    df = get_zillow_prop16()
    df2 = get_zillow_prop17()
    return df.append(df2)

def drop_columns(df):
    df = df[~df.longitude.isnull() | ~df.latitude.isnull()]
    return df.drop(columns=([\
        'airconditioningtypeid', 'architecturalstyletypeid',\
        'buildingclasstypeid', 'buildingqualitytypeid',
        'decktypeid', 'heatingorsystemtypeid', 'propertylandusetypeid',\
        'storytypeid', 'typeconstructiontypeid'\
    ]))

def remove_duplicates(df):
     return df.loc[:,~df.columns.duplicated()]

def make_csv(df):
    df.to_csv(r'/Users/kathrynsalts/codeup/methodologies/clustering/zillow.csv')
        

