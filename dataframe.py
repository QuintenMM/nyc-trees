import pandas as pd
import numpy as np
from pprint import pprint as pp




class YourClassname:

    def __init__(self, dataframe, max_cols, cons_width=50):
        self.df = dataframe
        self.df.sort_index()
        self.initiate_pandas(max_cols, cons_width)
        self.initiate_numpy(cons_width)


    @staticmethod
    def initiate_pandas(max_cols, cons_width):
        pd.set_option('display.max_columns', max_cols)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', cons_width)  # make output in console wider

    @staticmethod
    def initiate_numpy(console_width=640):
        # https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html
        np.set_printoptions(linewidth=console_width)

    def get_nan_count_column(self, column: str) -> int:
        return self.df[column].isna().sum()

    def get_unique_values_of_column(self, column) -> np.ndarray:
        if isinstance(self.df[column], pd.Series):
            return pd.unique(self.df[column])

    def get_overview_unique_count(self, just_print=False):
        column_with_unique_count_dictionary = dict()
        for column in self.df:
            column_with_unique_count_dictionary[column] = self.get_unique_values_of_column(column)
        if just_print:
            pp(column_with_unique_count_dictionary)
        else:
            return column_with_unique_count_dictionary

