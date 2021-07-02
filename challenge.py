# TODO : Run these commands before installing
import pandas as pd
import numpy as np


# TODO : Pull in the dataset
def get_data():
    url = 'https://raw.githubusercontent.com/becodeorg/GNT-Arai-2.31/master/content/additional_resources/datasets/NYC%20trees/data_100000.csv?token=AUDYSCLMQI2VVTFB5NPA3J3A43FKU'
    df1 = pd.read_csv(url, parse_dates=True)
    df1 = pd.DataFrame(df1)
    return df1


# TODO : clean the dataset
'''
   - The dataset contains no missing values ("" or null)
   - No duplicates.
   - Values are consolidated
   - Data format is correct
   - No blank spaces (ex: " I love python " => "I love python")
   -- sidetrack: The more rows of data you use, the better. However, pay attention that the more data you have, the longer each operation needs to execute.
   
'''


# drop all rows with any NaN and NaT values
def column_name(df1):
    column_names = list(df1)
    return column_names


Colum_name_list = column_name(get_data())


def drop_NaN(df1, Colum_name_list):
    df_temp = df1.dropna()
    df_Nan = []

    for name in Colum_name_list():
        df_Nan += df_temp[df_temp[name].str.contains("")]
    return df_Nan.shape()




# def drop_dub (df):
#     no_duplicates = df.drop_duplicates()
#     return no_duplicates
#
#
#
# # TODO : extra checks
# '''
# - Can values be consolidated? (e.g. Truck and truck refer to the same thing)
# - Are there some columns where most of the data is missing ?
# - Can you fill in some missing values ?
# - Is the date format correct?
# - Are some values integers that should be float or vice-versa ? Change the dtype.
# '''
# # TODO  : convert to .csv
